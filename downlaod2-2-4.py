import urllib.request as req
from urllib.parse import urlencode

#행안부의 게시판 RSS정보 가져오기 

API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values = {
    'ctxCd' : '1001'
}

print('before', values)
params = urlencode(values)
print('after', params) # format = json

url = API + '?' + params

print("요청 url : ", url) 

reqData = req.urlopen(url).read().decode('utf-8')


print(reqData)