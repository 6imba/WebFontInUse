import config
import mysql.connector

db_connection = mysql.connector.connect(host="localhost",user="simba",passwd="1234",database='WebFontInUse',auth_plugin='mysql_native_password')
db_cursor = db_connection.cursor()

def create_db_table():
    metadata_table_create_query = """CREATE TABLE if not exists meta_data (
        MetaDataID              int AUTO_INCREMENT PRIMARY KEY,
        CopyRight               LONGTEXT,
        Family                  varchar(255),
        SubFamily               varchar(255),
        VersionOfNameTable      LONGTEXT,
        FullName                varchar(255),
        PostScriptName          varchar(255),
        TrademarkNotice         varchar(255),
        ManufacturerName        varchar(255),
        DesignerName            varchar(255),
        Description             LONGTEXT,
        VendorUrl               LONGTEXT,
        DesignerUrl             LONGTEXT,
        LicenseDescription      LONGTEXT,
        LicenseUrl              LONGTEXT
    );"""
    db_cursor.execute(metadata_table_create_query)

    site_url_table_create_query = """
    CREATE TABLE if not exists site_url (
        SiteUrlID               int AUTO_INCREMENT PRIMARY KEY,
        RequestUrl              varchar(255),
        UrlType                 int,
        MetaDataID              int
    );"""
    db_cursor.execute(site_url_table_create_query)

    urlFontMap_table_create_query = """
    CREATE TABLE if not exists url_font_map (
        SourceUrl            int,
        FontUrl              int
    );"""
    db_cursor.execute(urlFontMap_table_create_query)

    print('Table created: meta_data,site_url,url_font_map.(if not exist)')

def insert_metadata(fontMetaDataList):
    metadata_table_insert_query = """INSERT INTO meta_data (
        CopyRight,Family,SubFamily,VersionOfNameTable,FullName,PostScriptName,
        TrademarkNotice,ManufacturerName,DesignerName,Description,VendorUrl,
        DesignerUrl,LicenseDescription,LicenseUrl
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    data = (fontMetaDataList[1], fontMetaDataList[17] if fontMetaDataList[17]!=None else fontMetaDataList[2] , fontMetaDataList[18] if fontMetaDataList[18]!=None else fontMetaDataList[3] ,fontMetaDataList[6],fontMetaDataList[5],fontMetaDataList[7],fontMetaDataList[8],fontMetaDataList[9],fontMetaDataList[10],fontMetaDataList[11],fontMetaDataList[12],fontMetaDataList[13],fontMetaDataList[14],fontMetaDataList[15])
    db_cursor.execute(metadata_table_insert_query,data)
    db_connection.commit() # when working with table data.
    print('\t\t\tRecord inserted: meta_data table.')
    return db_cursor.lastrowid

def insert_site_url(reqUrl,yrlType,metaID):
    site_url_insert_query = "INSERT INTO site_url (RequestUrl,UrlType,MetaDataID) VALUES (%s,%s,%s);"
    db_cursor.execute(site_url_insert_query,(reqUrl,yrlType,metaID))
    db_connection.commit() # when working with table data.
    print('\t\t\t\tRecord inserted: site_url table.')
    return db_cursor.lastrowid

def insert_url_font_map(sourceUrl,fontUrl):
    url_font_map_insert_query = "INSERT INTO url_font_map (SourceUrl,FontUrl) VALUES (%s,%s);"
    db_cursor.execute(url_font_map_insert_query,(sourceUrl,fontUrl))
    db_connection.commit() # when working with table data.
    print('\t\t\t\tRecord inserted: url_font_map table.')

def check_if_record_exist(para):
    record_count_query = "SELECT metadataid FROM meta_data WHERE postscriptname = (%s);"
    db_cursor.execute(record_count_query,[para])
    record = db_cursor.fetchone()
    if record == None:
        return [0,None]
    else:
        record_count = len(record)
        metadataid = record[0]
        return [record_count,metadataid]

def close_connection():
    db_connection.close()
