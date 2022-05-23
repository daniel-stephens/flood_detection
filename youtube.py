# Import pytube
from pytube import YouTube

# Specifying URL
url = "https://www.youtube.com/watch?v=CgVRnrk4Rv8&t=2460s"

# Getting the vido
video = YouTube(url)

# Getting highest videos
video = video.streams.get_highest_resolution()

# Downloading the video
video.download()