import os
import subprocess


def convert_mkv_to_mp4(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(".mkv"):
            mkv_path = os.path.join(folder_path, file)
            mp4_path = os.path.join(folder_path, file.rsplit(".", 1)[0] + ".mp4")
            subprocess.run(["ffmpeg", "-i", mkv_path, "-codec", "copy", mp4_path])

convert_mkv_to_mp4(f'/Users/craig/main/b99/Season 6/ep11')

# for i in range(1, 19):
#     convert_mkv_to_mp4(f'/Users/craig/main/b99/Season 6/ep{i}')

