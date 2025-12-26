import random


def simple_chance(success_chance: int) -> bool:
    return random.randint(1, 100) <= success_chance


def random_option(options: dict):
    return random.choices(list(options.keys()), weights=list(options.values()), k=1)[0]


def randomise_variable(variable: int, bound_change=0.5) -> int:
    lower_bound = variable * (1 - bound_change)
    upper_bound = variable * (1 + bound_change)
    return random.randint(int(lower_bound), int(upper_bound))
