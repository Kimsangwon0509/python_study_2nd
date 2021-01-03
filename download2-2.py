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

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료")