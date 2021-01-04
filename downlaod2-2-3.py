import urllib.request as req
from urllib.parse import urlencode


API = "https://api.ipify.org"

values = {
    'format' : 'json'
}

print('before', values)
params = urlencode(values)
print('after', params) # format = json

url = API + '?' + params

print("요청 url : ", url) # https://api.ipify.org?format=json

reqData = req.urlopen(url).read().decode('utf-8')


print(reqData) # {"ip":"14.36.47.31"}