import re
import os

import moviepy.editor as mp


def mp3_conversion(save_path):
    print("\n")
    for file in os.listdir(save_path):
        if re.search('mp4', file):
            try:
                mp4_file = os.path.join(save_path, file)
                mp3_file = os.path.join(save_path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_file)
                new_file.write_audiofile(mp3_file)
                os.remove(mp4_file)
            except (RuntimeError, Exception):
                print("Fuck... failed to convert file \"" + file + "\"")
