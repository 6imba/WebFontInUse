import requests
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
    state_json_file_read.close()
    json_dict["length"] = 0
    json_dict["time_taken"] = 0
    json_dict["site_font_urls"] = config.SITE_FONT_URLS
    print(json_dict)
    print('**************************************************************************************************')
    site_font_urls = open(json_dict["site_font_urls"])
    for iteration,row in enumerate(site_font_urls):
        if iteration+1 > json_dict["record_number"]:
            json_dict["record_number"] = iteration + 1
            json_str = json.dumps(json_dict) # json string...
            state_json_file_write = open(config.STATE_JSON, "w")
            state_json_file_write.write(json_str)
            state_json_file_write.close()
            
            print("\nRecord number: ", iteration+1)
            continue_step = process_url_record(row,json_dict)
            if continue_step == None: continue
            print(f"\t\t\t\t\t{json_dict['length']}{' urls. '}{'Time measured: '}{round(json_dict['time_taken'],2)}{' second...............................'}\n")

def process_url_record(row,json_dict):
    fontUrl = row.strip().split(',')[1]
    print("\tFontUrl: ",fontUrl)
    fontFileName = fontUrl.split('/')[-1]
    if "?" in fontFileName: fontFileName = fontFileName.split("?")[0] # check if there version mentioned in the font url, i.e fl-icons.woff?v=3.15.4
    # print("FontFileName: ",fontFileName)
    extension = fontFileName.split('.')[-1]
    # print("Extension: ",extension)
    fontFilePath = os.path.join(config.FONT_DIR,fontFileName)
    try:
        #time start...
        start = time.time()
        metaDataId = process_font_url(fontUrl,fontFilePath,extension) # None if not 'woff','woff2','ttf','otf.

        print("\t\t\tMetadata ===> ",metaDataId)
        siteUrl = row.strip().split(',')[0]
        sourceUrlId = db_con.insert_site_url(siteUrl,1,0)
        fontUrlId = db_con.insert_site_url(fontUrl,2,metaDataId)
        db_con.insert_url_font_map(sourceUrlId,fontUrlId)
        #time end...
        end = time.time()
        time_taken = end - start
        json_dict["length"] += 1
        json_dict["time_taken"] += time_taken
        return 1
    except Exception as e:
        if os.path.exists(fontFilePath): os.remove(fontFilePath) # delete the downloaded file if it couldn't be read by ttLib.TTFont()
        errMsg = f"Exception ==> {e}, ...... URL ==> {fontUrl}"
        print("\t\t\t",errMsg)
        save_in_log(config.ERROR_LOG,errMsg)

def process_font_url(fontUrl,fontFilePath,extension):
    if extension not in ['woff','woff2','ttf','otf']:
        errMsg = f"Invalid_FontFile_Extension, ...... URL ==> {fontUrl}"
        print("\t\t",errMsg)
        save_in_log(config.ERROR_LOG,errMsg)
        raise Exception("Invalid font file extension.") # only 'woff','woff2','ttf','otf' extension is allowed. 

    fontMetaDataList = retrieve_font_data(fontUrl,fontFilePath) #hold metadata



    if fontMetaDataList != None:
        [record_count,metadataid] =  db_con.check_if_record_exist(fontMetaDataList[7]) #skip duplication
        if record_count > 0:
            print("\t\t\tSkip inserting duplicate meta_data record.........")
            return metadataid



        metaDataId = db_con.insert_metadata(fontMetaDataList) #insert the meta data into database table.
        return metaDataId

def retrieve_font_data(fontUrl,fontFilePath):
    print("\t\tDownload file.............")
    try:
        response = requests.get(fontUrl, timeout=(21,60))
    except requests.exceptions.ConnectTimeout as e:
        save_in_log(config.SKIP_URL,fontUrl)
        errMsg = f"ConnectTimeout ==> 21 second. , {e}, ...... URL ==> {fontUrl}"
        print("\t\t\t",errMsg)
        save_in_log(config.ERROR_LOG,errMsg)
    except requests.exceptions.ReadTimeout as e:
        save_in_log(config.SKIP_URL,fontUrl)
        errMsg = f"ReadTimeout ==> 60 second.{e}, ...... URL ==> {fontUrl}"
        print("\t\t\t",errMsg)
        save_in_log(config.ERROR_LOG,errMsg)
    else:
        byteData = response.content
        file_obj = open(fontFilePath, 'wb')
        file_obj.write(byteData)
        file_obj.close()

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
print('**************************************************************************************************')
db_con.create_db_table()
state_management()
db_con.close_connection()

