import os

folder = '/Users/craig/main/yt'

for filename in os.listdir(folder):
    if filename.endswith('.mp4') and filename.startswith('ytdl.canehill.info - ') and filename.endswith(' (1080p).mp4'):
        new_name = filename.replace('ytdl.canehill.info - ', '').replace(' (1080p)', '')
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)