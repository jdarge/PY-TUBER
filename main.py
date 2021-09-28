# Programmed by Jan Darge.

# The user shall be allowed to download entire YouTube playlists or
# Single/Multiple videos by placing an individual video link.

import os
import re

import moviepy.editor as mp
from pytube import Playlist
from pytube import YouTube

SAVE_PATH = os.getcwd()

link = []
option = ''
mp3_option = False


def mp3_conversion():
    print("\n")
    for file in os.listdir(SAVE_PATH):
        if re.search('mp4', file):
            try:
                mp4_file = os.path.join(SAVE_PATH, file)
                mp3_file = os.path.join(SAVE_PATH, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_file)
                new_file.write_audiofile(mp3_file)
                os.remove(mp4_file)
            except (RuntimeError, Exception):
                print("Fuck... failed to convert file \"" + file + "\"")


flag = input("Do you want to specify the download folder? Default is your current working directory [Y/n]: ")
if flag == "y" or flag == "Y":
    SAVE_PATH = input("Enter a directory [Example: /home/user_name/Desktop]: ")

while True:
    option = input("\nPlease enter a digit representing an option below.\n"
                   "1. Playlist Downloader\n"
                   "2. Single/Multiple File Downloader\n\nInput: ")
    if option == '1' or option == '2':
        break
    print("Select a valid option from the list.\n\n")

extension = "mp4"

file_type = input("\nWould you like to download this video as an MP3 file? [Default: MP4] : ")
if file_type == "yes" or file_type == "Yes" or file_type == 'y' or file_type == 'Y':
    mp3_option = True
    print("MP3 FILE DOWNLOAD SELECTED...\n")

if option == '1':

    user_input = input("Enter a playlist: ")
    playlist = Playlist(user_input)
    print("\nDownloading...\n")

    if not mp3_option:
        for current in playlist.videos:
            try:
                print("Downloading: " + current.title)
                current.streams.filter(progressive=True, file_extension=extension) \
                    .order_by('resolution') \
                    .desc() \
                    .first(). \
                    download(SAVE_PATH)
            except (RuntimeError, Exception):
                print("Fuck... failed to download file \"" + current.title + "\"")

    else:
        for current in playlist.videos:
            try:
                print("Downloading: " + current.title)
                current.streams.filter(only_audio=True).first().download(SAVE_PATH)
            except (RuntimeError, Exception):
                print("Fuck... failed to download file \"" + current.title + "\"")

        mp3_conversion()

if option == '2':

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
                yt.streams.filter(progressive=True, file_extension=extension) \
                    .order_by('resolution') \
                    .desc() \
                    .first() \
                    .download(SAVE_PATH)
            except (RuntimeError, Exception):
                print("Fuck... failed to download file \"" + i + "\"")

    else:
        for i in link:
            try:
                yt = YouTube(i)
                print("Downloading: " + i)
                out_file = yt.streams.filter(only_audio=True).first().download(SAVE_PATH)
            except (RuntimeError, Exception):
                print("Fuck... failed to download file \"" + i + "\"")

        mp3_conversion()

print("\nProgram has concluded.")
