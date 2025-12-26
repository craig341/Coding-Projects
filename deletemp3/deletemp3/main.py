import os


def delete_mp3_files(folder):
    for file in os.listdir(folder):
        if file.endswith('.mp3'):
            os.remove(os.path.join(folder, file))




for i in range(1, 24):
    delete_mp3_files('/Users/craig/main/b99/Season 2/ep' + str(i))