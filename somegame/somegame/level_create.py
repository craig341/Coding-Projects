import os


def clear():
    os.system('clear')


floor = '[ ]'
empty_wall = ' '
wall = 'W'
void = '   '
new_line = '\n'
player = '[o]'
goal = '[@]'

level = 1

board_dict = {}
board_dimensions = (4, 5)

for x in range(board_dimensions[0]):
    for y in range(board_dimensions[1]):

        board_dict[(x, y)] = floor

        if y == board_dimensions[1] - 1:
            board_dict[(x, y + 0.5)] = new_line

        else:
            board_dict[(x, y + 0.5)] = empty_wall

board_dict[(0, 3)] = void
board_dict[(0, 4)] = void
board_dict[(3, 0)] = void
board_dict[(3, 1)] = void





def print_board(board=None, board_dims=None, board_level=level, message=''):
    if board is None:
        board = board_dict

    if board_dims is None:
        board_dims = board_dimensions

    if board_level:
        print(f'LEVEL: {board_level}')

    print('=' * 4 * board_dims[1])

    for tile in board:
        print(board[tile], end='')

    print('=' * 4 * board_dims[1])

    if message:
        print(message)


# print_board()

def level_maker():
    board_dict_lm = {}
    print_board(board_dict_lm)

    x_lm = 0
    y_lm = 0
    while True:
        input_lm = input()

        if not input_lm:
            if str(y_lm)[-1] == '5':
                board_dict_lm[(x_lm, y_lm)] = ' '
            else:
                board_dict_lm[(x_lm, y_lm)] = '[ ]'

        elif input_lm == 'w':
            board_dict_lm[(x_lm, y_lm)] = 'W'

        elif input_lm == 'x':
            board_dict_lm[(x_lm, y_lm)] = 'x'

        elif input_lm == '@':
            board_dict_lm[(x_lm, y_lm)] = '[@]'

        elif input_lm == 'v':
            board_dict_lm[(x_lm, y_lm)] = '   '

        elif input_lm == '\n' or input_lm == 'n':
            board_dict_lm[(x_lm, y_lm)] = '\n'
            x_lm += 1
            y_lm = -0.5

        else:
            board_dict_lm[(x_lm, y_lm)] = input_lm

        y_lm += 0.5

        clear()
        print(board_dict_lm)
        print_board(board=board_dict_lm, board_dims=(0, 0))

level_maker()




