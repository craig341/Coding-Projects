import os
from levels import all_levels


def clear():
    os.system('clear')


clear()

floor = '[ ]'
void = '   '
empty_wall = ' '
wall = 'W'
wall_spike = 'x'
floor_spike = '[x]'
new_line = '\n'
player = '[o]'
goal = '[@]'
power_up = '[.]'

level = 1
player_coords = ()
board_dict = {}
board_dict_copy = {}
board_dimensions = ()

hard_break = False


def print_board(board=None, board_dims=None, board_level=level, message=''):
    if board is None:
        board = all_levels[str(level)]['board']

    if board_dims is None:
        board_dims = all_levels[str(level)]['dimensions']

    if board_level:
        print(f'LEVEL: {board_level}')

    print(player_coords)

    print('=' * 4 * board_dims[1])

    for tile in board:
        print(board[tile], end='')

    print('=' * 4 * board_dims[1])

    if message:
        print(message)
        print('=' * 4 * board_dims[1])


def damage_player():
    global board_dict, board_dimensions, board_dict_copy, player_coords, level, player

    if player == '[0]':
        player = '[o]'
        board_dict[player_coords] = '[o]'

    elif player == '[o]':
        board_dict[player_coords] = board_dict_copy[player_coords]

        board_dict = all_levels[str(level)]['board'].copy()
        board_dict_copy = board_dict.copy()

        player_coords = all_levels[str(level)]['start']
        board_dict[player_coords] = player



def move_player(move_sequence, board=None):
    global player_coords, level, player, hard_break

    if board is None:
        board = all_levels[str(level)]['board']

    returned_move_sequence = ''

    if move_sequence == 'exit':
        raise 'EXIT GAME'

    for move in move_sequence:
        # if hard_break:
        #     break

        if move == 'w':
            end_coords = (player_coords[0] - 1, player_coords[1])

            if end_coords in board and board[end_coords] == void:
                break

            returned_move_sequence += 'w'

        elif move == 'a':
            end_coords = (player_coords[0], player_coords[1] - 1)

            if (player_coords[0], player_coords[1] - 0.5) in board and board[(player_coords[0], player_coords[1] - 0.5)] == wall:
                break

            elif (player_coords[0], player_coords[1] - 0.5) in board and board[(player_coords[0], player_coords[1] - 0.5)] == wall_spike:
                damage_player()
                break

            if end_coords in board and board[end_coords] == void:
                break

            returned_move_sequence += 'a'

        elif move == 's':
            end_coords = (player_coords[0] + 1, player_coords[1])

            if end_coords in board and board[end_coords] == void:
                break

            returned_move_sequence += 's'

        elif move == 'd':
            end_coords = (player_coords[0], player_coords[1] + 1)

            if (player_coords[0], player_coords[1] + 0.5) in board and board[(player_coords[0], player_coords[1] + 0.5)] == wall:
                break

            elif (player_coords[0], player_coords[1] + 0.5) in board and board[(player_coords[0], player_coords[1] + 0.5)] == wall_spike:
                damage_player()
                break

            if end_coords in board and board[end_coords] == void:
                break

            returned_move_sequence += 'd'

        elif move == ' ':
            end_coords = (player_coords[0], player_coords[1])
            returned_move_sequence += ' '

        else:
            continue

        if end_coords in board:
            board_dict[end_coords] = player

            if move != ' ':
                board_dict[player_coords] = board_dict_copy[player_coords]

        elif end_coords not in board:
            break

        if len(move_sequence) > 1 and end_coords in board:
            clear()
            print_board(board=board_dict, board_level=level)
            print(move_sequence)
            print(returned_move_sequence)
            input()

        player_coords = end_coords

        if board_dict_copy[player_coords] == goal:
            board[player_coords] = goal
            clear()
            print_board(board=board_dict, board_level=level, message='LEVEL CLEARED')
            input()
            level += 1
            break

        elif board_dict_copy[player_coords] == power_up:
            player = '[0]'
            board_dict[player_coords] = player
            board_dict_copy[player_coords] = floor

        elif board_dict_copy[player_coords] == floor_spike:
            damage_player()

            if board_dict_copy[player_coords] != floor_spike:
                break




def load_level(loaded_level):
    global board_dict, board_dimensions, board_dict_copy, player_coords, level

    print('=================')
    print()
    print(f'...LEVEL {loaded_level}...')
    print()
    print('=================')
    input()
    clear()

    board_dict = all_levels[str(loaded_level)]['board'].copy()
    board_dict_copy = board_dict.copy()
    board_dimensions = all_levels[str(loaded_level)]['dimensions']

    player = '[o]'
    player_coords = all_levels[str(level)]['start']
    board_dict[player_coords] = player

    while True:
        print_board(board=board_dict, board_dims=board_dimensions, board_level=loaded_level, message=all_levels[str(loaded_level)]['message'])
        move_sequence = input().lower()
        move_player(move_sequence=move_sequence)
        clear()

        if level != loaded_level:
            break

    load_level(loaded_level + 1)


def menu():
    while True:
        print('------TITLE------')
        print('=================')
        print()
        print('1. START')
        print()
        print('==================')
        choice = input().lower()
        clear()

        if choice == '1' or choice == 'start':
            load_level(loaded_level=1)
            break

#
# level = 6
# load_level(6)

menu()
