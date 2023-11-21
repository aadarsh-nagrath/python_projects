from pytube import YouTube

url = input("Enter the url of the video: ")

download_loc = "./"

instance = YouTube(url)

s = instance.streams.get_highest_resolution()

s.download()


print("Your video is downloaded")


