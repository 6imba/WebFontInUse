# https://requests.readthedocs.io/en/latest/
# response = requests.get(url, timeout=60)
# https://linuxpip.org/python-requests-timeout/#Timeouts_in_Python_requests

# connect timeout:
#     - The connect timeout is the number of seconds Requests will wait for your client to establish a connection to a server.

# read timeout:
#     - Once your client has connected to the server and sent the HTTP request, the read timeout is the number of seconds the client will wait for the server to send a response.
# Further: https://linuxpip.org/python-requests-timeout/#Timeouts_in_Python_requests



# import requests
# # url = 'http://localhost:3000/posts'
# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# try: 
#     # response = requests.get(url, timeout=(connect_timeout,read_timeout))
#     # response = requests.get(url, timeout=60)
#     # response = requests.get(url, timeout=3)
#     # response = requests.get(url, timeout=(21,60))
#     # response = requests.get(url, timeout=(3,60))
#     response = requests.get(url, timeout=(3,6))
#     response.raise_for_status()
# except requests.exceptions.Timeout as e:
#     print("Timeout ==> ", e)
#     print("Type ==> ", type(e))
# except Exception as e:
#     print("Exception ===> ", e)

# ConnectionTimeOut_Error ==>  HTTPSConnectionPool(host='m.unemployment.cmt.ohio.gov', port=443): Max retries exceeded with url: /css/fonts/SerifaBEFOP-Roman.otf (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x000001B9AA2D2E60>, 'Connection to m.unemployment.cmt.ohio.gov timed out. (connect timeout=21)'))
# ReadTimeOut_Error       ==>  HTTPConnectionPool(host='localhost', port=3000): Read timed out. (read timeout=5)
# ReadTimeOut_Error       ==>  HTTPSConnectionPool(host='m.unemployment.cmt.ohio.gov', port=443): Max retries exceeded with url: /css/fonts/SerifaBEFOP-Roman.otf (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x000001E2331D2E60>, 'Connection to m.unemployment.cmt.ohio.gov timed out. (connect timeout=3)'))



# Timeout ==>  HTTPConnectionPool(host='localhost', port=3000): Read timed out. (read timeout=6)
# Type ==>  <class 'requests.exceptions.ReadTimeout'> 

# Timeout ==>  HTTPSConnectionPool(host='m.unemployment.cmt.ohio.gov', port=443): Max retries exceeded with url: /css/fonts/SerifaBEFOP-Roman.otf (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x000001C181D12EF0>, 'Connection to m.unemployment.cmt.ohio.gov timed out. (connect timeout=3)'))
# Type ==>  <class 'requests.exceptions.ConnectTimeout'>




import requests
url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
try: 
    response = requests.get(url, timeout=(21,60))
    response.raise_for_status()
except requests.exceptions.ReadTimeout as e:
    print("ReadTimeout ==> ", e)
except requests.exceptions.ConnectTimeout as e:
    print("ConnectTimeout ==> ", e)
except Exception as e:
    print("Exception ===> ", e)