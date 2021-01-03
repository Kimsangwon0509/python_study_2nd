# 다른 에디터에서 한글이 출력이 안되는 부분을 위한 인코딩
import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
print('hi')

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5246%2F2020%2F10%2F14%2F0000020325_001_20201014171905308.jpg&type=sc960_832"
htmlURL = "https://google.com"

savePath1 = "E:/python-basicScraping/test1.jpg"
savePath2 = "E:/python-basicScraping/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()
saveFile1 = open(savePath1,'wb') # w: write, r : read, a : add
saveFile1.write(f)
#입출력 작업, DB connecction 후에는 리소스 반환을 꼭 해줘야 한다.
saveFile1.close()

with open('savePath2','wb') as saveFile2:
    saveFile2.write(f2)
    #파이썬 2.7 이후에 나온 lib로 with 문을 벗어날떄 자동으로 close가 되므로 생략이 가능하다.



print("다운로드 완료")

'''
urlretrieve 와 urlopen의 차이

urlopen 의 차이 변수를 먼저 할당 하고 파싱 해서 저장한다.
urlretrieve는 바로 다운로드 받아온다. 즉 저장이 된다음 open('r')을 읽어 온후 파싱해서 다시 저장한다. 

open사용을 권장한다.
'''