import os
import shutil


def move_all_mp3s(source_folder, target_folder, season, episode):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(".mp3"):
                source_path = os.path.join(root, file)
                # Avoid overwriting by renaming if needed
                base_name = os.path.splitext(file)[0]
                new_name = f"S{season}E{episode}.mp3"
                counter = 1
                while os.path.exists(os.path.join(target_folder, new_name)):
                    new_name = f"{base_name}_{counter}.mp3"
                    counter += 1
                shutil.copy2(source_path, os.path.join(target_folder, new_name))


target = "/Users/craig/Desktop/b99_audio"

season_episodes = {'Season 1': 22,
                   'Season 2': 23,
                   'Season 3': 23,
                   'Season 4': 22,
                   'Season 5': 22,
                   'Season 6': 18,
                   'Season 7': 13,
                   'Season 8': 10,
                   }
total = 0

for season in range(1, 9):
    for ep in range(1, season_episodes[f'Season {season}']+1):
        if season == 5:
            if ep in [12, 13]:
                continue
        elif season == 6 and ep == 17:
            continue
        source = f'/Users/craig/main/b99/Season {season}/ep{ep}'
        move_all_mp3s(source.strip(), target, season, ep)
        print(f'S{season}E{ep}')
        total += 1
    print()

print(total)