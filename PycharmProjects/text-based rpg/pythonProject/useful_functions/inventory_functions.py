from pythonProject.useful_functions.print_functions import text_boundary, clear, choice_text, rarity_text, view_item

from pythonProject.class_folder.equippables.weapons import weapon_dict
from pythonProject.class_folder.equippables.armour import armour_dict
from pythonProject.class_folder.equippables.potions import potion_dict
from pythonProject.class_folder.equippables.relics import relic_dict

from pythonProject.initial_variables import inv, player


def add_inv(item, amount=1):
    if amount == 0:
        return
    if item in inv.keys():
        inv[item] += amount
    else:
        inv[item] = amount


def remove_inv(item_key, amount=1):
    inv[item_key] -= amount
    if inv[item_key] == 0:
        del inv[item_key]


def inventory(mode='view'):
    text_boundary()
    print(f'{rarity_text('GOLD', 'gold')}:', player.gold)
    print('WEAPON:', player.weapon)
    print('ARMOUR:', player.armour)
    print('RELIC:', player.relic)
    for i, v in enumerate(inv):
        item_name = str(v)
        print(f'{i + 1}. {item_name} {'x' + str(inv[v]) if inv[v] > 1 else ''}')
    text_boundary()

    if mode == 'use':
        try:
            while True:
                print('Choose an item, (-1) to exit')
                item_index = input()

                if item_index.lower() == 'weapon':
                    return player.weapon
                elif item_index.lower() == 'armour':
                    return player.armour
                elif item_index.lower() == 'relic':
                    return player.relic

                if not item_index or not (  # input is empty ''
                        item_index.lstrip('-').isdigit() and item_index.count(
                    '-') <= 1):  # detects there is only 1 '-' and the rest of number is valid
                    print()
                    continue

                else:
                    if int(item_index) == -1:
                        clear()
                        return -1

                    item_index = int(item_index) - 1
                    if 0 <= item_index <= len(inv) - 1:
                        clear()
                        return item_index

                    else:
                        print()
                        continue

        except ValueError:
            print()


def use_inventory():
    is_player_obj = False  # item is not in player hand
    item_key = ''

    item_index = inventory('use')
    if item_index == -1:  # exit item choice
        return ['exit']
    if item_index.__class__.__name__ in ['Weapon', 'Armour', 'Relic']:  # item is in player hand
        if item_index == relic_dict['None']:
            clear()
            return ['exit']
        is_player_obj = True
    else:
        item_key = list(inv.keys())[item_index]  # determine item object

    item_class = item_key.__class__.__name__  # determines item class
    clear()
    inventory('view')

    if is_player_obj:
        option_labels = []
        add_to_inv = False
        item_class = item_index.__class__.__name__

        if ((player.weapon != weapon_dict['Fists'] and item_class == 'Weapon') or
                (player.armour != armour_dict['Naked'] and item_class == 'Armour') or
                (item_class == 'Relic')):
            option_labels.append('Add to Inventory')
            add_to_inv = True
        option_labels.extend(['View', 'Cancel'])

        choice = choice_text(f'Selected {item_index}', option_labels)  # item in hand can only be viewed
        if choice == 1 and add_to_inv:
            if item_class == 'Weapon':
                add_inv(player.weapon)
                player.weapon = weapon_dict['Fists']

            if item_class == 'Armour':
                add_inv(player.armour)
                player.armour = armour_dict['Naked']

            if item_class == 'Relic':
                add_inv(player.relic)
                player.relic = relic_dict['None']

        elif (choice == 2 and add_to_inv) or (choice == 1 and not add_to_inv):
            view_item(item_index, item_index.__class__.__name__)  # display item, auto clear

        return ['exit']

    if item_class == 'Weapon' or item_class == 'Armour' or item_class == 'Relic':  # weapon and armour cannot be used like potion
        choice = choice_text(f'Selected {item_key}', ['Switch', 'Drop', 'View', 'Cancel'])
        if choice == 1:
            if item_class == 'Weapon':
                if player.weapon == weapon_dict['Fists']:  # fists can't be added to inventory
                    del player.weapon
                else:
                    add_inv(player.weapon)
                player.weapon = item_key
                remove_inv(item_key)  # switched item must be removed from inventory, added to hand

            elif item_class == 'Armour':
                if player.armour == armour_dict['Naked']:  # naked can't be added to inventory
                    del player.armour
                else:
                    add_inv(player.armour)
                player.armour = item_key
                remove_inv(item_key)  # switched item must be removed from inventory, added to hand

                return ['exit']  # switching armour ends turn

            if item_class == 'Relic':
                if player.relic == relic_dict['None']:  # fists can't be added to inventory
                    del player.relic
                else:
                    add_inv(player.relic)
                player.relic = item_key
                remove_inv(item_key)  # switched item must be removed from inventory, added to hand

        elif choice == 2:
            drop_item(item_key)

        elif choice == 3:
            view_item(item_key, item_class)

        return ['exit']

    if item_class == 'Potion':
        return ['potion', item_key, item_class]


def summon_item():
    choice = choice_text('Item type', ['Weapon', 'Armour', 'Potion', 'Cancel'])
    clear()

    summon_item_dict, summon_item_class = weapon_dict, 'weapon'
    if choice == 2:
        summon_item_dict, summon_item_class = armour_dict, 'armour'
    elif choice == 3:
        summon_item_dict, summon_item_class = potion_dict, 'potion'

    elif choice == 5:
        return

    while True:
        try:
            print(f'Enter {summon_item_class} (x):')
            item_name = input().title()

            if item_name == 'X':
                break

            if item_name not in summon_item_dict:
                clear()
                continue

            print()
            print(f'How many {item_name}')
            amount = 1
            change_amount = input()
            if change_amount.isdigit():
                amount = change_amount
            print()

            add_inv(summon_item_dict[item_name], int(amount))
            print(f'Added {amount} {item_name} to inventory')
            input()
            clear()

            break

        except ValueError:
            clear()


def drop_item(item_key):
    inventory('view')
    amount = 1
    if inv[item_key] > 1:
        while True:
            try:
                amount = int(input(f'Remove how many {item_key}: '))
                while amount > inv[item_key] or amount < 0:
                    amount = int(input('Invalid: '))
                clear()
                inventory('view')
                break
            except ValueError:
                return

    confirmation = choice_text('Are you sure', ['Yes', 'No'])
    if confirmation == 1:
        remove_inv(item_key, amount)
