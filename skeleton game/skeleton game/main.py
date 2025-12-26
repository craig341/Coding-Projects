line = '======================='

turn = []
turn_text = {}

for i in range(1, 12):
    turn.append(f'turn_{i}')

    trump_suit = ''
    card_amount = 2 * i - 1
    trump_order = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

    if i >= 7:
        trump_suit = '\nNo Trump suit' if i == 11 else f'\nTrump suit: {trump_order[i - 7]}'
        card_amount = 13

    turn_text[turn[i - 1]] = [f'Each player gets {card_amount}' + (' card' if i == 1 else ' cards') + trump_suit,
                              card_amount]


def dealer_idx(turn_num):
    global player_num, player_list

    return (turn_num - 1) % player_num


def turn_n(n):
    global player_num, player_list

    print(line)
    print(f'TURN {n}')
    print("\n")

    player_n = n
    while player_n > player_num:
        player_n -= player_num

    print(f'{player_list[player_n - 1]} deals')
    print(turn_text[f'turn_{n}'][0])

    print("\n")

    predicted_w = [0 for i in player_list]
    start = dealer_idx(n) + 1
    counter = 0

    while counter < player_num:
        try:
            current_idx = (start + counter) % player_num

            if current_idx == (dealer_idx(n)) % player_num:

                predicted_dealer = int(input(f'{player_list[current_idx]} predicted wins: '))

                while predicted_dealer == turn_text[(f'turn_{n}')][1] - sum(predicted_w):
                    value = int(turn_text[f'turn_{n}'][1]) - sum(predicted_w)
                    predicted_dealer = int(input(f'Cannot say {value}: '))

                predicted_w[current_idx] = predicted_dealer
                return predicted_w

            predicted_w[current_idx] = int(input(f'{player_list[current_idx]} predicted wins: '))
            counter += 1

        except ValueError:
            print()
            print('Invalid input')
            print()


def calculate_score(a, p):
    if a == p:
        return p + 1
    elif a < p:
        return -(p - a + 1)
    elif a > p:
        return -1


def actual_wins(predicted_w, n):
    global player_num, player_list, scores
    actual_w = [0 for i in player_list]
    start = dealer_idx(n) + 1
    counter = 0

    if n > 7:
        n = 7

    while counter < player_num:

        current_idx = (start + counter) % player_num

        actual_w[current_idx] = int(input(f'{player_list[current_idx]} actual wins: '))
        counter += 1

        if counter == player_num and sum(actual_w) != 2 * n - 1:
            print()
            print('Scores do not match cards')
            choice = input('Continue? ').lower()
            print()

            while choice not in ['y', 'yes', 'n', 'no']:
                print('Invalid input')
                choice = input('Continue? ').lower()
                print()

            if choice == 'n' or choice == 'no':
                counter = 0

    for idx, num in enumerate(predicted_w):
        scores[idx] += calculate_score(actual_w[idx], num)

    print("\n")

    print('SCORES:')
    print()
    for i in range(len(player_list)):
        print(f'{player_list[i]}: {scores[i]}')

    return scores


def main():
    global player_num, player_list, scores

    print(line)

    player_num = int(input('How many players: '))
    print("\n")

    player_list = []
    scores = []

    for i in range(player_num):
        player_list.append(input(f'Player {i + 1} Name: '))
        scores.append(0)

    for i in range(1, 12):
        predicted_wn = turn_n(i)
        print("\n")

        scores = actual_wins(predicted_wn, i)


main()
