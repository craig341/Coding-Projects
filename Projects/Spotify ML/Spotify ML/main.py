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

basic_model = DecisionTreeRegressor()
basic_model.fit(train_X, train_y)
basic_pred = basic_model.predict(val_X)
basic_mae = mean_absolute_error(basic_pred, val_y)


optimised_model = DecisionTreeRegressor(max_leaf_nodes=500, max_depth=25, random_state=1)
optimised_model.fit(train_X, train_y)
