# lybrary to download the video
import pytube
import ssl

context = ssl._create_unverified_context()
urllib.request.urlopen(req,context=context)
# Ask for the url of video
url = input("Enter video url: ")
# We can take path as well, just uncomment the following line
# path = input("Enter path of storage: ")

# specify the storage path of video
path = "./video"

# magic line to download the video
pytube.YouTube(url).streams.get_highest_resolution().download(path)