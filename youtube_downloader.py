import pytube
# 다운받을 유투브 동영상
yt = pytube.YouTube("https://www.youtube.com/watch?v=2CMFjnuy9Kw")
videos = yt.streams.all()

#print('videos:', videos)

for i in range(len(videos)): #range(1,6)
    print(i,':', videos[i])

down_dir = 'E:\python-basicScraping'

videos[0].download(down_dir)
