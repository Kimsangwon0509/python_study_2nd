import urllib.request as req
from urllib.parse import urlparse

url = "https://www.inflearn.com/course/python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9B%B9-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%81%AC%EB%A1%A4%EB%A7%81/dashboard"

mem = req.urlopen(url)

# print(mem) <http.client.HTTPResponse object at 0x000001CDEFB89EB0>

# print(type(mem))  <class 'http.client.HTTPResponse'>


'''
print(type({}))
<class 'dict'>
print(type([]))
<class 'list'>
print(type(()))
<class 'tuple'>
'''

# print("geturl", mem.geturl())
# print("status", mem.status) # 응답코드 200 성공, 404 페이지 없음, 403 reject거절, 500 서버 에러
# print("Headers", mem.getheaders())
#print("info", mem.info())
#print("code", mem.getcode())
#print("read", mem.read(50)) # read 안에 숫자를 넣으면 받아올 양을 정한다.
#print("read", mem.read(100).decode("utf-8")) # 보통 디코딩을 해서 받아 온다.
print(urlparse(url))

