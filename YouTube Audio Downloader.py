#Extract Audio from Youtube Videos and Playlists
#To run on Windows or Mac you need to create an executable file with the help of PyInstaller
#To install PyInstaller run: pip install pyinstaller
#To create an executable: pyinstaller name.py --onefile
#For MacOS create exec with pyinstaller on mac and for Windows on Windows

import os
from pytube import YouTube, Playlist

def download_audio(video_url, destination):
    try:
        yt = YouTube(video_url)
        audio = yt.streams.filter(only_audio=True).first()

        out_file = audio.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(yt.title + " the video was successfully downloaded in .mp3 format")
        print("The file is saved in the folder: ", os.path.dirname(os.path.abspath(new_file)))
    except OSError:
        print("Error: Invalid folder to save the file.")
    except Exception as e:
        print("Error: Invalid video link.")


print("Youtube Audio Downloader - Made by MaxFax")
print("")

while True:
    input_type = input("Please select the type: \n1. Videos\n2. Playlist\n>> ")

    if input_type == '1':
        video_urls = input("Enter the link or links to the video, separated by commas, the sound of which you want to download: \n>> ")
        video_urls = video_urls.split(',')
        destination = input("Enter the path where to save (press enter for the current folder)\n>> ") or '.'

        for video_url in video_urls:
            download_audio(video_url.strip(), destination)
    elif input_type == '2':
        playlist_url = input("Enter the link to the playlist you want to download: \n>> ")
        destination = input("Enter the path where to save (press enter for the current folder)\n>> ") or '.'

        playlist = Playlist(playlist_url)

        for video_url in playlist.video_urls:
            download_audio(video_url, destination)
    else:
        print("C'mon! Choose 1 or 2 for the download type :)")
        continue

    choice = input("Do you want to continue? (yes/no)\n>> ")
    if choice.lower() != 'yes':
        break
