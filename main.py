# Programmed by Jan Darge.

# The user shall be allowed to download entire YouTube playlists or
# Single/Multiple videos by placing an individual video link.

import os

from playlist import playlist_run as playlist
from video import video_run as video

SAVE_PATH = os.getcwd()

option = ''
mp3_option = False

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

file_type = input("\nWould you like to download this video as an MP3 file? [Default: MP4] : ")
if file_type == "yes" or file_type == "Yes" or file_type == 'y' or file_type == 'Y':
    mp3_option = True
    print("MP3 FILE DOWNLOAD SELECTED...\n")

if option == '1':
    playlist(mp3_option, SAVE_PATH)


if option == '2':
    video(mp3_option, SAVE_PATH)

print("\nProgram has concluded.")
