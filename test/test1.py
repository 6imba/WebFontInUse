import requests

# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# url = 'http://localhost:3000/posts'
url = 'https://use.typekit.net/af/3e9574/000000000000000000010b62/27/l?subset_id=2&fvd=n9&v=3'

def process_url_record():
    try:
        retrieve_font_data(url)
    except Exception as e:
        print("Other Exception1. ===> ", e)

def retrieve_font_data(fontUrl):
    try:
        response = requests.get(fontUrl, timeout=(21,60))
    except requests.exceptions.ConnectTimeout as e:
        print("ConnectTimeout ==> 21 second.", e)
    except requests.exceptions.ReadTimeout as e:
        print("ReadTimeout ==> 6 second.", e)
    except Exception as e:
        print("Other Exception1.1. ===> ", e)
    else:
        byteData = response.content
        file_obj = open("./myfile.txt", 'wb')
        file_obj.write(byteData)
        file_obj.close()

# def save_in_log(fileName,content):
#     logfile = open(fileName,"a") #file_object
#     logfile.write(f"{content}\n") # writer_object of writer class.
#     logfile.close()


# Main Python Program Execution:
process_url_record()