import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


spotify_file_path = '/Users/craig/main/Code/Python/Projects/Spotify ML/dataset.csv'
raw_spotify_data = pd.read_csv(spotify_file_path)
spotify_data = raw_spotify_data[raw_spotify_data.popularity != 0]
spotify_data.reset_index(inplace=True)

y = spotify_data['popularity']
song_features = ['duration_ms', 'key', 'loudness', 'speechiness', 'acousticness',
                 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']
X = spotify_data[song_features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)


def get_mae(max_leaf_nodes, train_X=train_X, val_X=val_X, train_y=train_y, val_y=val_y) -> float:
    temp_model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    temp_model.fit(train_X, train_y)
    temp_model_pred = temp_model.predict(val_X)
    mae = mean_absolute_error(val_y, temp_model_pred)
    return mae


optimised_model = DecisionTreeRegressor(max_leaf_nodes=500, max_depth=25, random_state=1)
optimised_model.fit(train_X, train_y)
