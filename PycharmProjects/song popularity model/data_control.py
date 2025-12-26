import random
from main import spotify_data


def index_value_popularity() -> [(int, int)]:
    res = []
    for i, value in enumerate(spotify_data['popularity']):
        res.append((i, value))
    return res


def info(index) -> str:
    return (f'Index: {index} \n'
            f'Name: {spotify_data['track_name'][index]} \n'
            f'Artist/s: {spotify_data['artists'][index]} \n'
            f'Genre: {spotify_data['track_genre'][index]} \n'
            f'Popularity: {spotify_data['popularity'][index]} \n' # 0-100
            f'Duration: {spotify_data['duration_ms'][index]} \n'  # in ms
            f'Key: {spotify_data['key'][index]} \n'  # 0-11: chromatic C-B
            f'Loudness: {spotify_data['loudness'][index]} \n'  # in dB
            f'Speech: {spotify_data['speechiness'][index]} \n'  # 0.0-1.0 - 1: podcast, 0: instrumental
            f'Acoustic: {spotify_data['acousticness'][index]} \n'  # 0.0-1.0 - 1: acoustic, 0: electric
            f'Instruments: {spotify_data['instrumentalness'][index]} \n'  # 0.0-1.0, measure of vocals
            f'Live: {spotify_data['liveness'][index]} \n'  # 0.0-1.0, measure of audience presence 
            f'valence: {spotify_data['valence'][index]} \n'  # 0.0-1.0, happiness
            f'Tempo: {spotify_data['tempo'][index]} \n'  # in bpm
            f'Signature: {spotify_data['time_signature'][index]} \n'  # 3-7 - 3/4, 7/4
            )


def top_n_popular(n, highToLow=True):
    popularity_list = index_value_popularity()
    sorted_popularity_list = sorted(popularity_list, key=lambda x: x[1], reverse=(True if highToLow else False))

    for i, v in sorted_popularity_list[:n]:
        print(f'Song: {spotify_data['track_name'][i]} \t\t', end='')
        print(f'Artist: {spotify_data['artists'][i]} \t\t', end='')
        print(f'Popularity: {spotify_data['popularity'][i]} \t\t', end='')
        print(f'Index: {i}')


def song_dict_rand(n) -> dict:
    song_dict = {}
    seen = set()
    while len(seen) != n:

        rand_idx = random.randint(0, len(spotify_data))

        if spotify_data['track_name'][rand_idx] not in song_dict:
            song_dict[spotify_data['track_name'][rand_idx]] = rand_idx
        seen.add(rand_idx)

    return song_dict
