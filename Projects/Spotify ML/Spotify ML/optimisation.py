from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeRegressor
from main import train_X, train_y, val_X, val_y
from sklearn.metrics import mean_absolute_error


def get_mae(max_leaf_nodes, train_X=train_X, val_X=val_X, train_y=train_y, val_y=val_y) -> float:
    temp_model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    temp_model.fit(train_X, train_y)
    temp_model_pred = temp_model.predict(val_X)
    mae = mean_absolute_error(val_y, temp_model_pred)
    return mae


def grid_search() -> dict:
    model = DecisionTreeRegressor()

    param_grid = {
        'max_depth': list(n for n in range(20, 30, 1)),
        'max_leaf_nodes': list(n for n in range(400, 600, 25))
    }

    print('Loading grid-search . . .')
    grid_search = GridSearchCV(model, param_grid, cv=5)
    grid_search.fit(train_X, train_y)

    best_params = grid_search.best_params_  # 550, 27
    return best_params


def rand_search() -> dict:
    model = DecisionTreeRegressor()

    param_dist = {
        'max_depth': list(n for n in range(20, 30, 1)),
        'max_leaf_nodes': list(n for n in range(450, 900, 50))
    }

    print('Loading random-search . . .')
    random_search = RandomizedSearchCV(model, param_dist, n_iter=20, cv=20)
    random_search.fit(train_X, train_y)

    best_params = random_search.best_params_  # 500, 26
    return best_params
