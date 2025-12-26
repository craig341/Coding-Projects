import os
import subprocess


# project name is wrong but cba to change

def convert_mp4_to_mp3(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(".mp4"):
            mp4_path = os.path.join(folder_path, file)
            mp3_path = os.path.join(folder_path, file.rsplit(".", 1)[0] + ".mp3")
            subprocess.run(["ffmpeg", "-y", "-i", mp4_path, "-q:a", "0", "-map", "a", mp3_path])


for i in range(1, 24):
    # if i in []:
    #     continue
    convert_mp4_to_mp3('/Users/craig/main/b99/Season 2/ep' + str(i))
    print(f'ep{i} done')
