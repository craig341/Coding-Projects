import matplotlib.pyplot as plt


line = '============================'
colour_dict = {
    'default': '\033[0m',
    'gold': '\033[38;5;136m',
    'silver': '\033[38;5;246m',
    'bronze': '\033[38;5;173m',
    'red': '\033[38;5;1m',
    'black': '\033[38;5;16m',
    'predicted': '\033[38;5;117m',
    'actual': '\033[38;5;166m',
    'green': '\033[38;5;2m',
}

player_num = 0
turn = 1
turn_cards = 1
max_cards_each = 13
max_cards_each_isodd = True
total_cards = 52
player_list = []

turns_x = []
scores_y = {}

graphs_settings = True
custom_names_settings = True
auto_save_settings = True



class Player:
    def __init__(self, name, score=0, turn_pos=0, p_wins=0, a_wins=0):
        self.name = name
        self.score = score
        self.turn_pos = turn_pos
        self.p_wins = p_wins
        self.a_wins = a_wins


def c(text, colour):
    return f'{colour_dict[colour]}{text}{colour_dict['default']}'


def invalid(empty_print=True):
    print(f'{c('X', 'red')}Invalid input{c('X', 'red')}')

    if empty_print:
        print()


def start():
    global player_num, turn, max_cards_each, max_cards_each_isodd, total_cards
    print(line)

    while True:  # type proofing
        try:  # type proofing
            player_num = int(input('How many players: '))
            print()

            total_cards = int(input('How many decks: ')) * 52
            print('Cards:', total_cards)
            print()

            break  # type proofing

        except ValueError:  # type proofing
            invalid()

    if (total_cards // player_num) % 2 == 0:
        max_cards_each_isodd = False

    max_cards_each = total_cards // player_num

    while True:  # type proofing
        try:  # type proofing
            print(f"""Match length (max cards):
\t1. Normal (13)
\t2. Longest{' Odd' if not max_cards_each_isodd else ''} ({max_cards_each if max_cards_each_isodd else max_cards_each - 1}){'\n\t3. Custom' if max_cards_each_isodd else ''}{f'\n\t3. Longest Even ({max_cards_each})' if not max_cards_each_isodd else ''}{'\n\t4. Custom' if not max_cards_each_isodd else ''}""")

            choice = int(input())

            if choice == 1:  # 13
                max_cards_each = 13
                max_cards_each_isodd = True
                break  # type proofing

            elif choice == 2:  # longest odd
                max_cards_each = (total_cards // player_num) - (1 if not max_cards_each_isodd else 0)
                max_cards_each_isodd = True
                break  # type proofing

            elif choice == 3 and not max_cards_each_isodd:  # longest even
                max_cards_each = (total_cards // player_num)
                max_cards_each_isodd = False
                break  # type proofing

            elif (choice == 3 and max_cards_each_isodd) or (choice == 4 and not max_cards_each_isodd):  # custom
                print()
                while True:
                    max_cards_each = int(input('Custom max cards: '))

                    if max_cards_each <= (total_cards // player_num):
                        if max_cards_each % 2 == 0:
                            max_cards_each_isodd = False
                        else:
                            max_cards_each_isodd = True
                        break

                    invalid()

                break  # type proofing

            else:
                invalid()


        except ValueError:  # type proofing
            invalid()

    print()
    for i in range(player_num):
        if not custom_names_settings:
            player_name = f'player {i + 1}'
        else:
            player_name = input(f'Player {i + 1} Name: ')

        player_list.append(Player(name=player_name, turn_pos=i))


def turn_n(cards, trump_suit_key=-1):
    print(line)
    print(f'TURN: {turn}')
    print()

    print(f'Each player gets {cards} card{'s' if cards > 1 else ''}')

    if trump_suit_key != -1:
        trump_suit_msg_dict = {0: f'Trump suit: {c('♦Diamonds♦', 'red')}',
                               1: f'Trump suit: {c('♣Clubs♣', 'black')}',
                               2: f'Trump suit: {c('❤Hearts❤', 'red')}',
                               3: f'Trump suit: {c('♠Spades♠', 'black')}',
                               4: f'No trump suit',
                               }
        print(trump_suit_msg_dict[trump_suit_key])

    print()
    print()

    total_p_wins = 0
    total_a_wins = 0
    last_player = False

    player_list_turn_order = player_list.copy()
    player_list_turn_order.sort(key=lambda x: x.turn_pos)

    for player in player_list_turn_order:
        while True:  # type proofing
            try:  # type proofing
                if player.turn_pos == player_num - 1:
                    last_player = True

                p_wins = int(input(f'{player.name} {c('predicted', 'predicted')} wins ({total_p_wins}): '))

                if last_player and p_wins == (turn_cards - total_p_wins):
                    print(f'{c('X', 'red')}Cannot say {turn_cards - total_p_wins}{c('X', 'red')}')
                    continue

                if p_wins > turn_cards:
                    print(f'{c('X', 'red')}Cannot say {p_wins} (over total cards){c('X', 'red')}')
                    continue

                player.p_wins = p_wins
                total_p_wins += p_wins

                break  # type proofing

            except ValueError:  # type proofing
                invalid(empty_print=False)

    last_player = False
    print()
    print()

    while True:
        rerecord_a_wins = False
        for player in player_list_turn_order:
            while True:  # type proofing
                try:  # type proofing
                    if player.turn_pos == player_num - 1:
                        last_player = True

                    a_wins = int(input(f'{player.name} {c('actual', 'actual')} wins: '))

                    player.a_wins = a_wins
                    total_a_wins += a_wins

                    if last_player and total_a_wins != turn_cards:
                        print()
                        print(f'{c('X', 'red')}Scores ({total_a_wins}) do not match cards{c('X', 'red')}')
                        choice = input('Continue? ').lower()

                        while choice not in ['y', 'yes', 'n', 'no']:
                            print()
                            invalid(empty_print=False)
                            choice = input('Continue? ').lower()

                        if choice in ['n', 'no']:
                            print()
                            rerecord_a_wins = True
                            last_player = False
                            total_a_wins = 0

                    break  # type proofing

                except ValueError:  # type proofing
                    invalid(empty_print=False)

        if not rerecord_a_wins:
            break

    print()
    print()

    for player in player_list:
        if player.p_wins == player.a_wins:
            player.score += player.p_wins + 1

        elif player.p_wins < player.a_wins:
            player.score -= 1

        elif player.p_wins > player.a_wins:
            player.score -= (player.p_wins - player.a_wins + 1)

    print(f'SCORES:')
    print()

    player_list_score_order = player_list.copy()
    player_list_score_order.sort(key=lambda x: x.score, reverse=True)

    player_score_set = {player.score for player in player_list_score_order}
    unique_scores_list = sorted(list(player_score_set), reverse=True)

    for player in player_list_score_order:
        if player.score == unique_scores_list[0]:
            print(f'{c(f'{player.name}', 'gold')}: {player.score if player.score >= 0 else f'{c(player.score, 'red')}'}')

        elif player.score == unique_scores_list[1]:
            print(f'{c(f'{player.name}', 'silver')}: {player.score if player.score >= 0 else f'{c(player.score, 'red')}'}')

        elif player.score == unique_scores_list[2]:
            print(f'{c(f'{player.name}', 'bronze')}: {player.score if player.score >= 0 else f'{c(player.score, 'red')}'}')

        else:
            print(f'{player.name}: {player.score if player.score >= 0 else f'{c(player.score, 'red')}'}')

    for player in player_list:
        if player.turn_pos == 0:
            player.turn_pos = player_num - 1
        else:
            player.turn_pos -= 1
    #
    if graphs_settings:
        plt.clf()
        turns_x.append(turn)

        for player in player_list:
            scores_y[player.name].append(player.score)
            plt.plot(turns_x, scores_y[player.name], marker='o', label=player.name)



    plt.title('GRAPH OF DATA')
    plt.xlabel('Turns')
    plt.ylabel('Scores')
    plt.legend()
    # plt.show()
    # plt.pause(1)


# x = [1, 2, 3]
# y1 = [2, 3, 0]
# y2 = [-2, 0, 4]
#
#
# plt.ion()
# plt.plot(x, y1, marker='o')
# plt.plot(x, y2, marker='o')
# plt.show()


def settings():
    global graphs_settings, custom_names_settings, auto_save_settings

    while True:
        print(line)
        print(f'\t1. Graphs: {c('ON', 'green') if graphs_settings else c('OFF', 'red')}')
        print(f'\t2. Custom Names: {c('ON', 'green') if custom_names_settings else c('OFF', 'red')}')
        print(f'\t3. Auto-Save: {c('ON', 'green') if auto_save_settings else c('OFF', 'red')}')
        print(f'\t4. Exit')
        print(line)

        while True:  # type proofing
            try:
                choice = int(input())

                if choice == 1:
                    graphs_settings = True if graphs_settings is False else False
                    break

                if choice == 2:
                    custom_names_settings = True if custom_names_settings is False else False
                    break

                if choice == 3:
                    auto_save_settings = True if auto_save_settings is False else False
                    break

                if choice == 4:  # exit
                    return 'exit'

                else:
                    invalid()

            except ValueError:  # type proofing
                invalid()


def main():
    global turn_cards, turn

    print(line)
    print('\t1. Start')
    print('\t2. Load')
    print('\t3. Settings')
    print('\t4. Exit')
    print(line)

    while True:  # type proofing
        try:  # type proofing
            choice = int(input())

            if choice == 1:
                start()

                if graphs_settings:
                    for player in player_list:
                        scores_y[player.name] = []

                for _ in range(1, max_cards_each, 2):
                    turn_n(turn_cards)
                    turn_cards += 2
                    turn += 1

                if not max_cards_each_isodd:
                    turn_cards -= 1

                for i in range(5):
                    turn_n(turn_cards, i)
                    turn += 1

                input()

                print('code continued after graph')

                # if graphs_settings:
                    # turns_x.append(turn)

                    # for player in player_list:
                    #     scores_y[player.name].append(player.score)
                    #     plt.plot(turns_x, scores_y[player.name], marker='o', label=player.name)
                    #
                    # print(turns_x)
                    # print(scores_y)
                    #
                    # plt.title('GRAPH OF DATA')
                    # plt.xlabel('Turns')
                    # plt.ylabel('Scores')
                    #
                    # max_score = 0
                    # min_score = 0
                    #
                    # for player in player_list:
                    #     max_score = max(max_score, max(scores_y[player.name]))
                    #     min_score = min(min_score, min(scores_y[player.name]))
                    #
                    # plt.xticks(range(min(turns_x), max(turns_x) + 1))
                    # plt.yticks(range(min_score, max_score + 1))
                    #
                    # plt.legend()
                    # plt.show()


                break  # type proofing

            elif choice == 2:
                pass

            elif choice == 3:

                if settings() == 'exit':
                    break

            elif choice == 4:
                return 'exit'

            else:
                invalid()

        except ValueError:  # type proofing
            invalid()


print("""   ️             
  █████████  █████               ████            █████                       
 ███░░░░░███░░███               ░░███           ░░███                        
░███    ░░░  ░███ █████  ██████  ░███   ██████  ███████    ██████  ████████  
░░█████████  ░███░░███  ███░░███ ░███  ███░░███░░░███░    ███░░███░░███░░███ 
 ░░░░░░░░███ ░██████░  ░███████  ░███ ░███████   ░███    ░███ ░███ ░███ ░███ 
 ███    ░███ ░███░░███ ░███░░░   ░███ ░███░░░    ░███ ███░███ ░███ ░███ ░███ 
░░█████████  ████ █████░░██████  █████░░██████   ░░█████ ░░██████  ████ █████
 ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░  ░░░░░░     ░░░░░   ░░░░░░  ░░░░ ░░░░░ 
 """)

while True:
    if main() == 'exit':
        break


#
# if graphs_settings:
#     turns_x.append(turn)
#
#     # for player in player_list:
#     #     scores_y[player.name].append(player.score)
#     #     plt.plot(turns_x, scores_y[player.name], marker='o', label=player.name)
#
#     print(turns_x)
#     print(scores_y)
#
#     plt.title('GRAPH OF DATA')
#     plt.xlabel('Turns')
#     plt.ylabel('Scores')
#
#     max_score = 0
#     min_score = 0
#
#     for player in player_list:
#         max_score = max(max_score, max(scores_y[player.name]))
#         min_score = min(min_score, min(scores_y[player.name]))
#
#     plt.xticks(range(min(turns_x), max(turns_x) + 1))
#     plt.yticks(range(min_score, max_score + 1))
#
#     # plt.legend()
#     plt.show()

# ask:
# axis only increment by 1 or in integer values x
# how to reset a graph / remove all points x
# plt.show stops rest of code to run. Breaks the code loop
# get 3d text art for title x
# red text if neg score x
