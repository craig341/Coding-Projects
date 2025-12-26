import random

total_wines = 1000
total_prisoners = 10

p = random.randint(0, total_wines - 1) #com


def print_support_text(support_text, allowed, end='\n'):
    if allowed:
        print(support_text, end=end)


def main(poisoned_wine_idx, allow_support_text=True):
    wines = []
    prisoners = []

    class Wine:
        def __init__(self, idx, poisoned):
            self.idx = idx
            self.poisoned = poisoned

    for i in range(total_wines):
        wines.append(Wine(i, False))

    wines[poisoned_wine_idx].poisoned = True

    class Prisoner:
        def __init__(self, prisoner_num, codes, willDie):
            self.prisoner_num = prisoner_num
            self.willDie = willDie
            self.codes = codes

        def drink(self, wine):
            self.codes.append(wine.idx)

            if wine.poisoned:
                self.willDie = True

    for i in range(total_prisoners):
        prisoners.append(Prisoner(i + 1, [], False))

    prisoner_to_drink = 0
    for rounds in range(1, 4):
        wines_per_prisoner = total_wines // (total_prisoners ** rounds)
        wpp_counter = wines_per_prisoner

        for wine in wines:
            if prisoner_to_drink >= 10:
                prisoner_to_drink = 0

            prisoners[prisoner_to_drink].drink(wine)

            wpp_counter -= 1

            if wpp_counter == 0:
                prisoner_to_drink += 1
                wpp_counter = wines_per_prisoner

    print_support_text('Poisoned wine: ' + str(poisoned_wine_idx) + '\n', allow_support_text)

    possible_poisoned_wines = []

    # for prisoner in prisoners:
    #     if prisoner.willDie:
    #         print_support_text(f"Prisoner {prisoner.prisoner_num} dies", allow_support_text)
    #
    #         # prisoner_codes = prisoner.codes
    #         # prisoner_codes = set(prisoner_codes)
    #         # possible_poisoned_wines.append(prisoner_codes)
    #
    #         # print_support_text(sorted(list(prisoner_codes)), allow_support_text)
    #         # print_support_text('\n', allow_support_text)

    for prisoner in prisoners:
        print(f"Prisoner {prisoner.prisoner_num} dies")
        print(prisoner.codes)
        print()


    print_support_text('Wines in all sets: ', allow_support_text, end='')

    if len(possible_poisoned_wines) == 1:
        ppw = possible_poisoned_wines[0]
        print_support_text(ppw, allow_support_text)
        print_support_text('\n', allow_support_text)

        print_support_text('1 person died, meaning the other 2 numbers in the wine idx are the same, or wine idx was 0', allow_support_text)
        for num in ppw:
            if num == 0 or num % 111 == 0:
                print_support_text('Poisoned wine must be: ' + str(num), allow_support_text)

                if not allow_support_text:
                    return num


    elif len(possible_poisoned_wines) == 2:
        ppw = possible_poisoned_wines[0].intersection(possible_poisoned_wines[1])
        print_support_text(ppw, allow_support_text)
        print_support_text('\n', allow_support_text)

        print_support_text('2 people died, meaning 1 other number repeats', allow_support_text)

        string_ppw = sorted(list(ppw))
        for i, num in enumerate(string_ppw):
            zeroes = ''
            for _ in range(3 - len(str(string_ppw[i]))):
                zeroes += '0'

            string_ppw[i] = zeroes + str(num)

        reduced_ppw = []
        ppw = sorted(list(ppw))

        for i, num in enumerate(string_ppw):
            if (num.count(num[0]) > 1) or (num.count(num[1]) > 1):
                reduced_ppw.append(ppw[i])

        print_support_text('Poisoned wine must be in: ' + str(reduced_ppw), allow_support_text)

        if not allow_support_text:
            return reduced_ppw


    elif len(possible_poisoned_wines) == 3:
        ppw = possible_poisoned_wines[0].intersection(possible_poisoned_wines[1], possible_poisoned_wines[2])
        print_support_text(ppw, allow_support_text)

        if not allow_support_text:
            return ppw


if __name__ == '__main__':
    main(123, False)
