from urllib import request
from fontTools import ttLib
import os
import config
import time
import mysql.connector
import db_con
import json

def state_management():
    state_json_file_read = open(config.STATE_JSON) # json file...
    json_dict = json.load(state_json_file_read) # python dictionary...
    json_dict["length"] = 0
    json_dict["time_taken"] = 0
    state_json_file_read.close()
    site_font_urls = open(json_dict["site_font_urls"])
    for iteration,row in enumerate(site_font_urls):
        if iteration+1 > json_dict["record_number"]:
            json_dict["record_number"] = iteration + 1
            json_str = json.dumps(json_dict) # json string...
            state_json_file_write = open(config.STATE_JSON, "w")
            state_json_file_write.write(json_str)
            state_json_file_write.close()

            print("Record number: ", iteration+1)
            process_url_record(row,json_dict)
            print(f"{json_dict['length']}{' urls. '}{'Time measured: '}{round(json_dict['time_taken'],2)}{' second...............................'}\n")

def process_url_record(row,json_dict):
            fontUrl = row.strip().split(',')[1]
            print("FontUrl: ",fontUrl)
            fontFileName = fontUrl.split('/')[-1]
            if "?" in fontFileName: fontFileName = fontFileName.split("?")[0] # check if there version mentioned in the font url, i.e fl-icons.woff?v=3.15.4
            extension = fontFileName.split('.')[-1]
            fontFilePath = os.path.join(config.FONT_DIR,fontFileName)
            try:
                #time start...
                start = time.time()
                metaDataId = process_font_url(fontUrl,fontFilePath,extension)
                print("Metadata ===> ",metaDataId)
                # print('option-----------------------------------------')
                if metaDataId != None:
                    siteUrl = row.strip().split(',')[0]
                    sourceUrlId = db_con.insert_site_url(siteUrl,1,0)
                    fontUrlId = db_con.insert_site_url(fontUrl,2,metaDataId)
                    # print(sourceUrlId)
                    # print(fontUrlId)
                    db_con.insert_url_font_map(sourceUrlId,fontUrlId)
                #time end...
                end = time.time()
                time_taken = end - start
                json_dict["length"] += 1
                json_dict["time_taken"] += time_taken
            except Exception as e:
                # print('error----------------------------------------')
                if os.path.exists(fontFilePath): os.remove(fontFilePath) # delete the downloaded file if it couldn't be read by ttLib.TTFont()
                errMsg = f"Error ==> {e}, ...... URL ==> {fontUrl}"
                print(errMsg)
                # errMsg = [e.__class__,fontUrl]
                # print(f"Error Message ==> {e.__class__}{' url=>'}{fontUrl}")
                save_in_log(config.ERROR_LOG,errMsg)
            # print(iteration," Record...")

def process_font_url(fontUrl,fontFilePath,extension):
    if extension not in ['woff','woff2','ttf','otf']: return # only 'woff','woff2','ttf','otf' extension is allowed.    
    fontMetaDataList = retrieve_font_data(fontUrl,fontFilePath) #hold metadata
    # print('MetaData: ',fontMetaDataList)
    metaDataId = db_con.insert_metadata(fontMetaDataList) #insert the meta data into database table.
    return metaDataId

def retrieve_font_data(fontUrl,fontFilePath):
    # Download font_file from given url.
    req = request.Request(fontUrl)
    req.add_header('User-Agent', 'Mozilla/5.0')
    try:
        reqConn = request.urlopen(req, timeout=60)
    except:
        save_in_log(config.SKIP_URL,fontUrl)
        raise Exception("Timeout")
    else:
        byteData = reqConn.read()
        file = open(fontFilePath, 'wb')
        file.write(byteData)
        file.close()
        # Read the downloaded font_file and fetch the metadata.
        fontFile = ttLib.TTFont(fontFilePath)   
        fontMetaDataList = []
        fontMetaDataList.append(fontUrl) # add url of the fontFile whose meta data is getting fetched
        for i in range(0,19):
            fontMetaDataList.append(fontFile['name'].getDebugName(i))
        os.remove(fontFilePath) # delete local downloaded font_file once meta is fetched.
        return fontMetaDataList

def save_in_log(fileName,content):
    logfile = open(fileName,"a") #file_object
    logfile.write(f"{content}\n") # writer_object of writer class.
    logfile.close()


# Main Python Program Execution:
db_con.create_db_table()
state_management()
db_con.close_connection()
