import os


def clear():
    os.system('clear')


clear()

tile = '[ ]'
empty_wall = ' '
new_line = '\n'
player = '[o]'
goal = '[@]'

level = '1-1'

# empty board

board_dict = {}
board_dimensions = (3, 10)

for x in range(board_dimensions[0]):
    for y in range(board_dimensions[1]):
        board_dict[(x, y)] = tile

        if y == board_dimensions[1] - 1:
            board_dict[(x, y + 0.5)] = new_line
        else:
            board_dict[(x, y + 0.5)] = empty_wall

board_dict[(1, 9)] = goal

board_dict_copy = board_dict.copy()

print(board_dict)


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


def move_player(move_sequence, board=None):
    global player_coords, level

    if board is None:
        board = board_dict

    # end_coords = ()
    returned_move_sequence = ''

    for move in move_sequence:
        if move == 'w':
            end_coords = (player_coords[0] - 1, player_coords[1])
            returned_move_sequence += 'w'

        elif move == 'a':
            end_coords = (player_coords[0], player_coords[1] - 1)
            returned_move_sequence += 'a'

        elif move == 's':
            end_coords = (player_coords[0] + 1, player_coords[1])
            returned_move_sequence += 's'

        elif move == 'd':
            end_coords = (player_coords[0], player_coords[1] + 1)
            returned_move_sequence += 'd'

        else:
            continue


        if end_coords in board:
            board_dict[end_coords] = player
            board_dict[player_coords] = board_dict_copy[player_coords]

            clear()
            print_board()

        else:
            break

        if len(move_sequence) > 1 and end_coords in board:
            clear()
            print_board()
            print(move_sequence)
            print(returned_move_sequence)
            input()

        player_coords = end_coords

        # input(f'player_coords: {player_coords}')
        if check_player() == 'goal':
            clear()
            print_board(message='LEVEL CLEARED')
            input()
            level = '1-2'

            # clear()
            # print_board(message='next level')
            # input()

            break


def check_player():
    if board_dict_copy[player_coords] == goal:
        return 'goal'


player_coords = (2, 0)
board_dict[player_coords] = player

while True:
    print_board()
    move_sequence = input().lower()
    move_player(move_sequence=move_sequence)
    clear()
