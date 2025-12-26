square_dict = {
    'tl': 'a',
    'tr': 'b',
    'bl': 'c',
    'br': 'd',
    'no': 'X'
}

cube_face = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
]

target_face = [
    ['a', 'X', 'c'],
    ['X', 'X', 'X'],
    ['b', 'X', 'd'],
]

cube_dict = {
    (0, 0): square_dict['tl'], (0, 1): square_dict['no'], (0, 2): square_dict['tr'],
    (1, 0): square_dict['no'], (1, 1): square_dict['no'], (1, 2): square_dict['no'],
    (2, 0): square_dict['bl'], (2, 1): square_dict['no'], (2, 2): square_dict['br']
}


def show_cube(cube):
    for row in cube:
        for square in row:
            colour_dict = {
                'a': '\033[38;5;1m',
                'b': '\033[38;5;4m',
                'c': '\033[38;5;2m',
                'd': '\033[38;5;3m',
                'X': '\033[38;5;15m'
            }

            def colour_text(text):
                return f'{colour_dict[text]}{text}{'\033[38;5;15m'}'

            print(colour_text(cube_dict[square]), end=' ')
        print()


def algo(base):
    tl = cube_dict[(0, 0)]  # rotating squares anti-clockwise
    tr = cube_dict[(0, 2)]
    bl = cube_dict[(2, 0)]
    br = cube_dict[(2, 2)]

    cube_dict[(0, 0)] = tr
    cube_dict[(2, 0)] = tl
    cube_dict[(2, 2)] = bl
    cube_dict[(0, 2)] = br
    """"""

    base_destination = {  # swapping the base back
        (0, 0): (2, 0),
        (2, 0): (2, 2),
        (2, 2): (0, 2),
        (0, 2): (0, 0),
    }

    temp = cube_dict[base_destination[base]]

    cube_dict[base_destination[base]] = cube_dict[base]
    cube_dict[base] = temp
    """"""

    tl = cube_dict[(0, 0)]  # updating square_dict
    tr = cube_dict[(0, 2)]
    bl = cube_dict[(2, 0)]
    br = cube_dict[(2, 2)]

    square_dict['tl'] = tl
    square_dict['tr'] = tr
    square_dict['bl'] = bl
    square_dict['br'] = br


def update_square_dict():
    tl = cube_dict[(0, 0)]
    tr = cube_dict[(0, 2)]
    bl = cube_dict[(2, 0)]
    br = cube_dict[(2, 2)]

    square_dict['tl'] = tl
    square_dict['tr'] = tr
    square_dict['bl'] = bl
    square_dict['br'] = br


def verify_cube():
    for i in range(3):
        for j in range(3):
            if cube_dict[cube_face[i][j]] == target_face[i][j]:
                continue
            else:
                return False
    return True


code = 'd a b c'

show_cube(cube_face)
print()

while True:
    new_code = f'{cube_dict[0, 0]} {cube_dict[0, 2]} {cube_dict[2, 0]} {cube_dict[2, 2]}'
    print(new_code)

    if new_code == code:
        # solution_list.append()
        input('cow')

    base = input('Enter square: ')
    print()
    key = ()
    for k, v in cube_dict.items():
        if v == base:
            key = k
            break

    algo(key)
    show_cube(cube_face)
    print()

    if verify_cube():
        break
