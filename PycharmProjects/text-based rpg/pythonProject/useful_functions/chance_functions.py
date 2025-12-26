import random


def randint(a, b):
    return random.randint(a, b)


def simple_chance(success_chance):
    if 0 < randint(1, 100) <= success_chance:
        return True
    return False


def random_option(options):
    items = list(options.keys())
    weights = list(options.values())

    chosen = random.choices(items, weights=weights, k=1)[0]

    return chosen


def randomise_variable(variable, bound_change=0.5):
    lower_bound = variable * (1 - bound_change)
    upper_bound = variable * (1 + bound_change)
    return randint(int(lower_bound), int(upper_bound))





