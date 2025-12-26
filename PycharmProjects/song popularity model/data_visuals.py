from sklearn.tree import plot_tree
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from main import song_features, spotify_data, optimised_model
from main import train_X, train_y, val_X, val_y


def max_leaf_node_graph():
    print('Loading max_leaf_node graph . . .')
    leaf_nodes = list(n * 50 for n in range(1, 41))

    train_errors = []
    val_errors = []

    for i in leaf_nodes:
        temp_model = DecisionTreeRegressor(max_leaf_nodes=i, random_state=1)
        temp_model.fit(train_X, train_y)

        train_pred = temp_model.predict(train_X)
        val_pred = temp_model.predict(val_X)

        train_errors.append(mean_absolute_error(train_y, train_pred))
        val_errors.append(mean_absolute_error(val_y, val_pred))

    plt.plot(leaf_nodes, train_errors, label='Training')
    plt.plot(leaf_nodes, val_errors, label='Validation')

    plt.xlabel("Maximum Leaf nodes")
    plt.ylabel("Mean Average Error")
    plt.title("Effect of Maximum Leaf Nodes")

    plt.legend()
    plt.show()


def max_depth_graph():
    print('Loading max_depth Graph . . .')
    leaf_nodes = list(n * 2 for n in range(1, 41))

    train_errors = []
    val_errors = []

    for i in leaf_nodes:
        temp_model = DecisionTreeRegressor(max_depth=i, random_state=1)
        temp_model.fit(train_X, train_y)

        train_pred = temp_model.predict(train_X)
        val_pred = temp_model.predict(val_X)

        train_errors.append(mean_absolute_error(train_y, train_pred))
        val_errors.append(mean_absolute_error(val_y, val_pred))

    plt.plot(leaf_nodes, train_errors, label='Training')
    plt.plot(leaf_nodes, val_errors, label='Validation')

    plt.xlabel("Maximum depth")
    plt.ylabel("Mean Average Error")
    plt.title("Effect of Maximum Leaf Nodes")

    plt.legend()
    plt.show()


def visual_tree():
    print('Loading visual tree . . .')
    plt.figure(figsize=(12, 8))
    plot_tree(optimised_model, filled=True, feature_names=song_features, rounded=True)
    plt.show()


def bar_graph(song_dict):
    print('Loading song-accuracy bar graph . . .')
    predicted_popularity = []
    actual_popularity = []

    for popularity_index in song_dict.values():
        song_features_data = spotify_data.loc[popularity_index, song_features]

        prediction = optimised_model.predict([song_features_data])[0]
        predicted_popularity.append(prediction)

        actual = spotify_data.loc[popularity_index, 'popularity']
        actual_popularity.append(actual)

    songs = list(song_dict.keys())
    bar_width = 0.35
    x = np.arange(len(songs))

    fig, ax = plt.subplots(figsize=(10, 6))

    bars1 = ax.bar(x, actual_popularity, width=bar_width, label='Actual Popularity', color='b')
    bars2 = ax.bar(x + bar_width, predicted_popularity, width=bar_width, label='Predicted Popularity', color='g')

    ax.set_xlabel('Songs')
    ax.set_ylabel('Popularity Score')
    ax.set_title('Actual vs Predicted Popularity of Songs')

    ax.set_xticks(x + bar_width / 2)
    ax.set_xticklabels(songs, rotation=45, ha='right')

    ax.legend()
    plt.show()


max_leaf_node_graph()