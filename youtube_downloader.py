import pytube
import os
#파이썬을 실행하면서 별도의 프로세스를 생성해서 터미널이나 커맨드에 있는 것을 실행하고 반환 받을수 있다.
import subprocess


# 다운받을 유투브 동영상
yt = pytube.YouTube("https://www.youtube.com/watch?v=2CMFjnuy9Kw")
videos = yt.streams.all()

#print('videos:', videos)

for i in range(len(videos)): #range(1,6)
    print(i,':', videos[i])

cNum = int(input("다운 받을 화질은?(0~17 입력)"))

down_dir="E:\python-basicScraping"

videos[cNum].download(down_dir)

#다운로드 후에 ffmpeg을 mp3파일로 변환 시킬것 (옵션)
#ffmpeg이 해당 파일에 있어야 한다.

newFileNmae = input("변환 할 mp3 파일명은?")
oriFileNmae = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileNmae),
    os.path.join(down_dir,newFileNmae + '.mp3'),
])

print("동영상 다운로드 및 mp3 변환 완료")