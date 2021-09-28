from mp3_convert import mp3_conversion as mpc
from pytube import YouTube

link = []


def video_run(mp3_option, save_path):
    while True:
        temp = input("Enter a YouTube link, or input -1: ")
        if temp == '-1':
            break
        link.append(temp)

    print("\nDownloading...\n")

    if not mp3_option:
        for i in link:
            try:
                yt = YouTube(i)
                print("Downloading: " + i)
                yt.streams.filter(progressive=True, file_extension="mp4") \
                    .order_by('resolution') \
                    .desc() \
                    .first() \
                    .download(save_path)
            except (RuntimeError, Exception):
                print("Fuck... failed to download file \"" + i + "\"")

    else:
        for i in link:
            try:
                yt = YouTube(i)
                print("Downloading: " + i)
                yt.streams.filter(only_audio=True).first().download(save_path)
            except (RuntimeError, Exception):
                print("Fuck... failed to download file \"" + i + "\"")

        mpc(save_path)
