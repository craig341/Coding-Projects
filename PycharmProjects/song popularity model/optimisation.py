from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeRegressor
from main import train_X, train_y


def grid_search() -> dict:
    model = DecisionTreeRegressor()

    param_grid = {
        'max_depth': list(n for n in range(19, 30, 1)),
        'max_leaf_nodes': list(n for n in range(400, 600, 25))
    }

    print('Loading grid-search . . .')
    grid_search = GridSearchCV(model, param_grid, cv=5)  # 5-fold cross-validation
    grid_search.fit(train_X, train_y)

    best_params = grid_search.best_params_  # 550, 27
    return best_params


def rand_search() -> dict:
    model = DecisionTreeRegressor()

    param_dist = {
        'max_depth': list(n for n in range(20, 30, 1)),
        'max_leaf_nodes': list(n for n in range(500, 3000, 500))
    }

    print('Loading random-search . . .')
    random_search = RandomizedSearchCV(model, param_dist, n_iter=20, cv=20)
    random_search.fit(train_X, train_y)

    best_params = random_search.best_params_  # 500, 26
    return best_params
