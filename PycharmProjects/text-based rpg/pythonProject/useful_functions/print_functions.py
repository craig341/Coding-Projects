import os
from sys import exit
from colorama import Fore, Style

from pythonProject.classes import rarity_dict


def clear():
    os.system('clear')


def text_boundary(pos=None, length=30, middle=None):
    if pos == 'end':
        print()

    if middle:
        half_boundary = '=' * (length // 2 - len(middle) // 2)
        print(half_boundary + middle + half_boundary)
    else:
        print('=' * length)

    if pos == 'start':
        print()


def healthbar(entity, length=20, player=True, fill_bar=0):
    health = entity.health
    if entity.health < 0:
        health = 0

    remaining_bars = round(health / entity.max_health * length)
    lost_bars = length - remaining_bars - fill_bar
    print(f'{entity.name.upper()}: {health}/{entity.max_health}')
    print(f'|{rarity_text(f'{remaining_bars * '█'}', 'player' if player else 'enemy')}'
          f'{fill_bar * (rarity_text('█', 'enemy'))}'
          
          f'{rarity_text((lost_bars * '_'), 'player' if player else 'enemy')}|')


def story_text(text, header='', auto_clear=True, ask_input=True):
    text_boundary(middle=header, pos='start', length=(len(text)+5 if len(text)+5 > 30 else 30))
    print(text)
    text_boundary(pos='end', length=(len(text)+5 if len(text)+5 > 30 else 30))

    if ask_input:
        input()

    if auto_clear:
        clear()


def death():
    clear()
    text_boundary('start')
    print('you dead')
    text_boundary('end')
    exit(0)


def choice_text(header='', option_labels=list, auto_clear=True, boundary=False):
    text_boundary(length=len(header)) if boundary else print('', end='')

    if header != 'no header':
        print(header + ':')

    for i, option in enumerate(option_labels, start=1):
        print(f'    {i}. {option}')

    text_boundary(length=len(header)) if boundary else print('', end='')

    while True:
        user_input = input()
        print()

        if user_input.isdigit():
            user_choice = int(user_input)
            if 1 <= user_choice <= len(option_labels):
                if auto_clear:
                    clear()
                return user_choice

        elif user_input.lower() == 'inv':
            return 'inv'


def rarity_text(text: str, rarity: str):
    return f'{rarity_dict[rarity]}{text}{rarity_dict['default']}'


def view_item(item, item_class, current=False, ask_input=True, auto_clear=True):
    text_boundary()
    print(rarity_text(item.name, item.rarity) + (' (Current)' if current else ''))
    print(f'"{item.description}"')
    print()
    print('PRICE:', rarity_text(item.price, 'gold'))

    if item_class == 'Weapon':
        print('DAMAGE:', item.damage)
        print('SPEED:', item.speed)
        print('ACCURACY:', item.aim)
        print('CRIT CHANCE:', item.crit_chance)
        print('DURABILITY:', (item.durability if item.durability != -1 else 'UNBREAKABLE'))

    elif item_class == 'Armour':
        print('DEFENSE:', item.defense)
        print('SPEED:', item.speed)
        print('ACCURACY:', item.aim)
        print('CRIT:', item.crit_chance)
        print('DURABILITY:', (item.durability if item.durability != -1 else 'UNBREAKABLE'))

    elif item_class == 'Potion':
        attributes = ['STRENGTH', 'HEALTH', 'SPEED', 'ACCURACY']
        for i, v in enumerate(item.attribute_changes):
            print(f'{attributes[i]}: {v}')
        print('DURATION:', item.duration)
    text_boundary()

    if not current:
        if ask_input:
            input()
        if auto_clear:
            clear()


def choice_story_text(header='', option_labels=list):
    story_text(text=header, auto_clear=False, ask_input=False)
    choice = choice_text(header='no header', option_labels=option_labels)

    return choice


def gift(item, gifter, amount=1):
    from pythonProject.useful_functions.inventory_functions import add_inv

    story_text(f'{gifter} gave you{' x' + str(amount) if amount > 1 else ''} {item}')
    add_inv(item=item, amount=amount)

