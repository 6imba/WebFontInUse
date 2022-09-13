# from urllib import request

# url1 = "https://jsonplaceholder.typicode.com/users"

# req1 = request.Request(url1)
# print(req1)
# reqConn1 = request.urlopen(req1)
# print(reqConn1)
# byteData1 = reqConn1.read()
# print(byteData1)

# file_obj_1 = open("./file_store/test.json", 'wb')
# file_obj_1.write(byteData1)
# file_obj_1.close()


# from urllib import request
# url2 = "https://static-webfonts.myfonts.com/kit/RooneySans_normal_normal/font.woff2"
# req2 = request.Request(url2)
# print(req2)
# req2.add_header('User-Agent', 'Mozilla/5.0')
# reqConn2 = request.urlopen(req2)
# print(reqConn2)
# byteData2 = reqConn2.read()
# print(byteData2)
# file_obj_2 = open("./file_store/font.woff2", 'wb')
# file_obj_2.write(byteData2)
# file_obj_2.close()


# from urllib.request import Request, urlopen
# req3 = Request(
#     url = 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/fonts/slick.woff',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# reqConn3 = urlopen(req3)
# byteData3 = reqConn3.read()
# file_obj_3 = open("./file_store/slick.woff", 'wb')
# file_obj_3.write(byteData3)
# file_obj_3.close()


# from urllib.request import Request, urlopen
# req4 = Request(
#     url = 'https://jsonplaceholder.typicode.com',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# reqConn4 = urlopen(req4)
# byteData4 = reqConn4.read()
# file_obj_4 = open("./file_store/index.html", 'wb')
# file_obj_4.write(byteData4)
# file_obj_4.close()



# from urllib.request import Request, urlopen
# req4 = Request(
#     url = 'https://www.linotype.com/css/fonts/fontello.woff2?30518695',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# reqConn4 = urlopen(req4)
# byteData4 = reqConn4.read()
# file_obj_4 = open("./file_store/fontello.woff2", 'wb')
# file_obj_4.write(byteData4)
# file_obj_4.close()



# from urllib.request import Request, urlopen
# req4 = Request(
#     url = 'https://www.linotype.com/css/fonts/fontello.woff2?30518695',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# reqConn4 = urlopen(req4)
# byteData4 = reqConn4.read()
# file_obj_4 = open("./file_store/fontello.txt", 'wb')
# file_obj_4.write(byteData4)
# file_obj_4.close()



# Reference:
    # https://fluentprogramming.com/python-urllib-error-httperror-http-error-403-forbidden/
    # https://www.pythonpool.com/urllib-error-httperror-http-error-403-forbidden/


# mod security ===> scraping bot ===> detecting/blocking ===> include user-agent/s in our scraper -> headers = {'User-Agent': 'Mozilla/5.0'}

# The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.



# from urllib.request import Request, urlopen
# req4 = Request(
#     url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# try:
    # reqConn4 = urlopen(req4, timeout=0.01)
#     byteData4 = reqConn4.read()
#     file_obj_4 = open("./file_store/fontello.txt", 'wb')
#     file_obj_4.write(byteData4)
#     file_obj_4.close()
# except Exception as e:
#     raise Exception("Timeout 0.01 second.")
#     print(e)



# from urllib.request import Request, urlopen
# from socket import timeout
# req4 = Request(
#     url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# try:
#     # reqConn4 = urlopen(req4, timeout=2)
#     reqConn4 = urlopen(req4)
# except Exception as e:
#     if isinstance(e.reason, timeout):
#         raise Exception("Timeout 2 second.")
#     else:
#         raise Exception("Other exception.")
# else:
#     byteData4 = reqConn4.read()
#     file_obj_4 = open("./file_store/fontello.txt", 'wb')
#     file_obj_4.write(byteData4)
#     file_obj_4.close()


# from urllib.request import Request, urlopen
# from socket import timeout
# req4 = Request(
#     url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# try:
#     reqConn4 = urlopen(req4, timeout=2) # <urlopen error timed out> ==> type: <class 'urllib.error.URLError'>
#     # reqConn = urlopen(req4) # <urlopen error [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond> =-==> type: 
#     # reqConn = urlopen(req4) #Network error: <urlopen error [Errno 11001] getaddrinfo failed> ===> type: <class 'urllib.error.URLError'>
# except Exception as e:
#     # print(e) 
#     print(type(e))
#     # raise Exception(e)
# else:
#     byteData4 = reqConn4.read()
#     file_obj_4 = open("./file_store/fontello.txt", 'wb')
#     file_obj_4.write(byteData4)
#     file_obj_4.close()



# from urllib.request import Request, urlopen
# from urllib.error import HTTPError, URLError
# import socket
# import requests
# from tornado.gen import TimeoutError
# req4 = Request(
#     url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# try:
#     reqConn4 = urlopen(req4, timeout=2) # <urlopen error timed out> ==> type: <class 'urllib.error.URLError'>
#     # reqConn = urlopen(req4) # <urlopen error [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond> =-==> type: 
#     # reqConn = urlopen(req4) #Network error: <urlopen error [Errno 11001] getaddrinfo failed> ===> type: <class 'urllib.error.URLError'>
# # except HTTPError as e:
# #     # print(e) 
# # #     # print(type(e))
# #     print("HTTP-Error") 
# # #     # raise Exception(e)
# except requests.Timeout as e:
#     print("TimeOut-Error") 
# except requests.RequestException as e:
#     print("URL-Error") 
# # except URLError as e:
# # #     # print(e) 
# # # #     # print(type(e))
# #     print("URL-Error") 
# # #     # raise Exception(e)
# # #     # print(isinstance(e.reason, socket.timeout))

# #     if isinstance(e.reason, socket.timeout):
# #         print("TimeOut-Error") 
# #     else:
# #         print("URL-Error") 

# else:
#     byteData4 = reqConn4.read()
#     file_obj_4 = open("./file_store/fontello.txt", 'wb')
#     file_obj_4.write(byteData4)
#     file_obj_4.close()



# from urllib.request import Request, urlopen
# from urllib.error import URLError
# import socket

# req = Request(
#     url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )


# try:
#     response = urlopen(req, timeout=1)
# except Exception as e:
#     print(e) # <urlopen error timed out>
#     print(type(e)) # <class 'urllib.error.URLError'>
#     print(e.getcode) # <class 'urllib.error.URLError'>


# try:
#     reqConn4 = urlopen(req4, timeout=1) # <urlopen error timed out> ==> type: <class 'urllib.error.URLError'>
#     # reqConn4 = urlopen(req4)
# # except URLError as e:
# #     print(e.code)
# #     if isinstance(e.reason, socket.timeout):
# #         print("TimeOut-Error", e) 
# #     else:
#         # print("URL-Error", e) 
# except Exception as e:
#     print("Other Exception: ",e)
# else:
#     byteData4 = reqConn4.read()
#     file_obj_4 = open("./fontello.txt", 'wb')
#     file_obj_4.write(byteData4)
#     file_obj_4.close()


# import urllib3
# http = urllib3.PoolManager()
# response = http.request('GET', 'https://static.wixstatic.com/ufonts/c59cfc_157f288f30c743499a8cf98575c10d0b/woff2/file.woff2')
# print(response)
# print(type(response)) # <class 'urllib3.response.HTTPResponse'>
# print(response.status)# 200
# print(type(response.status)) # <class 'int'>
# print(response.data)
# print(type(response.data)) # <class 'bytes'>

# import urllib3
# http = urllib3.PoolManager()
# response = http.request('GET', 'https://static.wixstatic.com/ufonts/c59cfc_157f288f30c743499a8cf98575c10d0b/woff2/file.woff2')
# byteData = response.data
# file_obj = open("./fontello.txt", 'wb')
# file_obj.write(byteData)
# file_obj.close()



# import urllib3
# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# # url = 'https://static.wixstatic.com/ufonts/c59cfc_157f288f30c743499a8cf98575c10d0b/woff2/file.woff2'
# http = urllib3.PoolManager()
# try: 
#     req = http.request('GET', url)
#     print(req.status)
# except Exception as e:
#     print(('Occurred Error:', e)) # ('Occurred Error:', MaxRetryError("HTTPSConnectionPool(host='m.unemployment.cmt.ohio.gov', port=443): Max retries exceeded with url: /css/fonts/SerifaBEFOP-Roman.otf (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x00000196398922F0>, 'Connection to m.unemployment.cmt.ohio.gov timed out. (connect timeout=<object object at 0x00000196377046C0>)'))"))
#     print(type(e)) # <class 'urllib3.exceptions.MaxRetryError'>
#     print(req.status)


# import urllib3
# url = 'https://m.unemployment.cmt.ohio.gov/css/fonts/SerifaBEFOP-Roman.otf'
# # url = 'https://static.wixstatic.com/ufonts/c59cfc_157f288f30c743499a8cf98575c10d0b/woff2/file.woff2'
# http = urllib3.PoolManager()
# try: 
#     req = http.request('GET', url)
#     print(req.status)
# except Exception as e:
#     print(('Occurred Error:', e)) # ('Occurred Error:', MaxRetryError("HTTPSConnectionPool(host='m.unemployment.cmt.ohio.gov', port=443): Max retries exceeded with url: /css/fonts/SerifaBEFOP-Roman.otf (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x00000196398922F0>, 'Connection to m.unemployment.cmt.ohio.gov timed out. (connect timeout=<object object at 0x00000196377046C0>)'))"))
#     print(type(e)) # <class 'urllib3.exceptions.MaxRetryError'>
    # print(e.reason) # (<urllib3.connection.HTTPSConnection object at 0x000002343F9E23E0>, 'Connection to m.unemployment.cmt.ohio.gov timed out. (connect timeout=<object object at 0x000002343D8546C0>)')



# if req.status
# byteData = req.data
# file_obj = open("./fontello.txt", 'wb')
# file_obj.write(byteData)
# file_obj.close()