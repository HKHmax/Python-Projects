from pytube import YouTube
from pytube import Playlist
import re
import os
path = input("Please choose the directory to save your videos eg 'C:\...' ")
playlist_link = input('Please input your YouTube Playlist link')
choice = input('You like to download videos or sound track only? Please enter video / sound')
subtitle_choice = input("Would you like to download the English subtitles - Yes / No")
single = input('Would you like to download a playlist or single video? Enter 1 for playlist and 0 for single video') 
playlist = Playlist(playlist_link)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
videolist = playlist.video_urls
print('There are ', str(len(videolist)), 'videos in your playlist')
print('Start Downloading:')
n = 1
if choice == 'video':
    for video in videolist:
        yt = YouTube(video)
        print(str(n) + '. '+ yt.title) #set the title of the YouTube Videos
        if len(yt.streams.filter(subtype = 'mp4', res = '1080p', progressive = True)) != 0:
            yt.streams.filter(subtype = 'mp4', res = '1080p', progressive = True).first().download(r'{}'.format(path))
        elif len(yt.streams.filter(subtype = 'mp4', res = '720p', progressive = True)) != 0:
            yt.streams.filter(subtype = 'mp4', res = '720p', progressive = True).first().download(r'{}'.format(path))
        elif len(yt.streams.filter(subtype = 'mp4', res = '320p', progressive = True)) != 0:
            yt.streams.filter(subtype = 'mp4', res = '320p', progressive = True).first().download(r'{}'.format(path))
        elif len(yt.streams.filter(subtype = 'mp4', res = '144p', progressive = True)) != 0:
            yt.streams.filter(subtype = 'mp4', res = '144p', progressive = True).first().download(r'{}'.format(path))
        else:
            print('There are suitable video quality for you to download')
        n = n + 1
    m = 1
    if subtitle_choice == 'Yes':
        for video in videolist:
            yt = YouTube(video)
            caption = yt.captions['en']
            srt = caption.generate_srt_captions()
            file = open(os.path.join(dire, str(m)+'.srt'), 'w', encoding = 'utf-8')
            file.write(srt)
            file.close()
            print(str(m) + '. ' + yt.title + '.srt')
            m = m + 1
    print("Subtitles Download Complete")    
    print('Download Complete')

if choice == 'sound':
    for video in videolist:
        caption = yt.captions['en']
        n = n + 1
    print('Download Complete')

