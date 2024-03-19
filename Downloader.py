from pytube import YouTube 
import os

title = ''

def download(URL):
    global title
    yt = YouTube(str(URL))
    if not URL:
        yt = YouTube( 
            str(input("Enter the URL: \n>> "))) 

    video = yt.streams.filter(only_audio=True).first() 
    title = video.title

    destination = 'temp'
    out_file = video.download(output_path=destination) 

    base, ext = os.path.splitext(out_file) 
    try:
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 
    except:
        os.remove(out_file)
        print(f"{out_file} has been removed")

    return title + " has been successfully downloaded."
