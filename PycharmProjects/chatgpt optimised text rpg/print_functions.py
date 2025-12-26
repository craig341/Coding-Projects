import os
from colorama import Fore, Style


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def text_boundary(pos=None, length=30, middle=None):
    line = '=' * length
    if middle:
        padding = (length - len(middle)) // 2
        line = '=' * padding + middle + '=' * padding
    if pos == 'start':
        print()
    print(line)
    if pos == 'end':
        print()


def healthbar(entity, length=20, player=True):
    health = max(entity.health, 0)
    filled = round(health / entity.max_health * length)
    empty = length - filled
    bar_color = Fore.GREEN if player else Fore.RED
    print(f"{entity.name.upper()}: {health}/{entity.max_health}")
    print(f"|{bar_color}{'█' * filled}{Style.RESET_ALL}{'_' * empty}|")


def story_text(text):
    clear()
    text_boundary(pos='start', length=max(len(text) + 4, 30))
    print(text)
    text_boundary(pos='end', length=max(len(text) + 4, 30))
    input()
    clear()


def death():
    clear()
    text_boundary('start')
    print("You have died. Game over!")
    text_boundary('end')
    exit(0)


def choice_text(header='', option_labels=None, auto_clear=True):
    if header:
        print(header + ":")
    for idx, option in enumerate(option_labels, start=1):
        print(f"    {idx}. {option}")
    while True:
        choice = input("Choose an option: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(option_labels):
            if auto_clear:
                clear()
            return int(choice)
