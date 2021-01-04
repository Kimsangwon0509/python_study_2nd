import urllib.request as dw

videoUrl = "https://s.pstatic.net/static/www/mobile/edit/2021/0104/cropImg_728x360_51674876994323474.jpeg"
savePath = "E:/python-basicScraping/test2.jpeg"

f = dw.urlopen(videoUrl).read()

with open('savePath','wb') as saveFile2:
    saveFile2.write(f)

# jpeg파일이므로 저장이 안된듯 보임
