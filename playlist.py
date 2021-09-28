from mp3_convert import mp3_conversion as mpc
from pytube import Playlist


def playlist_run(mp3_option, path):
    user_input = input("Enter a playlist: ")
    playlist = Playlist(user_input)
    print("\nDownloading...\n")

    if not mp3_option:
        for current in playlist.videos:
            try:
                print("Downloading: " + current.title)
                current.streams.filter(progressive=True, file_extension="mp4") \
                    .order_by('resolution') \
                    .desc() \
                    .first(). \
                    download(path)
            except (RuntimeError, Exception):
                print("Fuck... failed to download file \"" + current.title + "\"")

    else:
        for current in playlist.videos:
            try:
                print("Downloading: " + current.title)
                current.streams.filter(only_audio=True).first().download(path)
            except (RuntimeError, Exception):
                print("Fuck... failed to download file \"" + current.title + "\"")

        mpc(path)
