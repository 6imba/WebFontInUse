# https://requests.readthedocs.io/en/latest/
# response = requests.get(url, timeout=60)
# https://linuxpip.org/python-requests-timeout/#Timeouts_in_Python_requests

# connect timeout:
#     - The connect timeout is the number of seconds Requests will wait for your client to establish a connection to a server.

# read timeout:
#     - Once your client has connected to the server and sent the HTTP request, the read timeout is the number of seconds the client will wait for the server to send a response.
# Further: https://linuxpip.org/python-requests-timeout/#Timeouts_in_Python_requests


# import requests

# # url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# url = 'https://static.wixstatic.com/ufonts/c59cfc_157f288f30c743499a8cf98575c10d0b/woff2/file.woff2'

# response = requests.get(url)
# print(response) # <Response [200]>
# # print(response.text) # response content in text
# # print(response.content) # response content in binary formate
# print(response.url) # https://static.wixstatic.com/ufonts/c59cfc_157f288f30c743499a8cf98575c10d0b/woff2/file.woff2
# print(response.status_code) # 200
# print(response.request) # <PreparedRequest [GET]>
# print(response.ok)
# print(response.headers['content-type'])
# print(response.encoding)
# print(response.json())
# response.close()

# print(response.raise_for_status()) # 200






# import requests
# try: 
#     response = requests.get('https://static.wixstatic.com/ufonts/c59cfc_157f288f30c743499a8cf98575c10d0b/woff2/file.woff2')
#     byteData = response.content
#     file_obj = open("./file.woff2", 'wb')
#     file_obj.write(byteData)
#     file_obj.close()



# import requests
# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# try: 
#     response = requests.get(url)
# except Exception as e:
#     print("Occurred error ===> ",e)
# # Error types:
#     # Occurred error ===>  HTTPSConnectionPool(host='m.unemployment.cmt.ohio.gov', port=443): Max retries exceeded with url: /css/fonts/SerifaBEFOP-Roman.otf (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000016529542E30>: Failed to establish a new connection: 
#         # [Errno 11001] getaddrinfo failed'))
#     # Occurred error ===>  HTTPSConnectionPool(host='m.unemployment.cmt.ohio.gov', port=443): Max retries exceeded with url: /css/fonts/SerifaBEFOP-Roman.otf (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x00000171CBBB2E30>, 'Connection to m.unemployment.cmt.ohio.gov timed out. (connect timeout=None)'))



# import requests
# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# try: 
#     response = requests.get(url)
#     response.raise_for_status()
# except Exception as e:
#     print("Occurred error ===> ",e)
# # Error types:
#     # Occurred error ===>  HTTPSConnectionPool(host='m.unemployment.cmt.ohio.gov', port=443): Max retries exceeded with url: /css/fonts/SerifaBEFOP-Roman.otf (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000016529542E30>: Failed to establish a new connection: 
#         # [Errno 11001] getaddrinfo failed'))
#     # Occurred error ===>  HTTPSConnectionPool(host='m.unemployment.cmt.ohio.gov', port=443): Max retries exceeded with url: /css/fonts/SerifaBEFOP-Roman.otf (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x00000171CBBB2E30>, 'Connection to m.unemployment.cmt.ohio.gov timed out. (connect timeout=None)'))



# import requests
# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# try: 
#     response = requests.get(url)
#     response.raise_for_status()
# except Exception as e:
#     print(response.status_code)




# import requests
# import urllib3
# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# try: 
#     response = requests.get(url)
#     response.raise_for_status()
# except urllib3.connection.HTTPSConnection as e:
#     print(response.status_code)


# import requests
# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# try: 
#     response = requests.get(url)
#     response.raise_for_status()
# except Exception as e:
#     print(e)



# import requests
# import time
# url1 = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# url2 = 'https://msale24.com/wp-content/themes/flatsome/assets/css/icons/fl-icons.woff2?v=3.15.4'
# url3 = 'https://panditindraji.com/wp-content/themes/bridge/css/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0'
# url4 = 'http://www.nerdporn.sexy/wp-content/themes/hueman/assets/front/fonts/titillium-lightitalic-webfont.woff'
# url5 = 'https://karibecompany.com/wp-content/plugins/wd-instagram-feed/css/tenweb-fonts/fonts/tenweb.ttf?4znsty'
# url6 = 'https://www.wyb.ac.lk/wp-content/plugins/social-icons-widget-by-wpzoom/assets/font/Genericons.ttf'
# url7 = 'https://static.tildacdn.com/tild6262-6331-4564-b430-376466633630/Geometria-ExtraBold.woff'

# urls = [url1,url2,url3,url4,url5,url6,url7]
# urls = [url1]

# for url in urls:
#     start = time.time()
#     try: 
#         # response = requests.get(url, proxies={'http': '222.255.169.74:8080'}, timeout=60)
#         response = requests.get(url, timeout=6)
#         response.raise_for_status()
#     except requests.exceptions.Timeout as e:
#         end = time.time()
#         print("Time taken ==> ", end-start)
#         print("Timeout ==> ", e)
#     except Exception as e:
#         end = time.time()
#         print("Time taken ==> ", end-start)
#         print("Exception ===> ", e)




# import requests
# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# try: 
#     response = requests.get(url, timeout=6)
#     response.raise_for_status()
# except requests.exceptions.Timeout as e:
#     print("Timeout ==> ", e)
# except Exception as e:
#     print("Exception ===> ", e)


# import requests
# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# try: 
#     response = requests.get(url, timeout=60)
#     response.raise_for_status()
# except requests.exceptions.Timeout as e:
#     print("Timeout ==> ", e)
# except Exception as e:
#     print("Exception ===> ", e)




import requests
url = 'http://localhost:3000/posts'
try: 
    response = requests.get(url, timeout=60)
    response.raise_for_status()
except requests.exceptions.Timeout as e:
    print("Timeout ==> ", e)
except Exception as e:
    print("Exception ===> ", e)