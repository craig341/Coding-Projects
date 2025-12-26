from pythonProject.useful_functions.print_functions import clear, story_text, rarity_text, choice_text, view_item
from pythonProject.useful_functions.chance_functions import random_option
from pythonProject.useful_functions.inventory_functions import inventory, add_inv

from pythonProject.class_folder.equippables.weapons import weapon_dict
from pythonProject.class_folder.equippables.armour import armour_dict

from pythonProject.class_folder.services.chests import chest_dict

from pythonProject.initial_variables import player


def choice_chest(chest_type, choices):
    clear()
    story_text(f'You found a {rarity_text(chest_type, chest_dict[chest_type].rarity)} Chest')

    items_only = []
    items_only_names = []
    option_labels = []

    for item in choices:
        if type(item) is not int:
            items_only.append(item)
            items_only_names.append(rarity_text(item.name, item.rarity))
            item = rarity_text(item.name, item.rarity)
        else:
            item = f'+{rarity_text(item, 'gold')} gold'

        option_labels.append(item)

    option_labels.append('View item')

    while True:
        choice = choice_text('Choose your item', option_labels, boundary=True)
        clear()

        if choice == len(option_labels):
            choice = choice_text('View item', items_only_names, boundary=True)
            item_view = items_only[choice-1]

            view_item(item_view, item_view.__class__.__name__)

            clear()
            continue

        else:
            item_view = items_only[choice - 1]
            view_item(item_view, item_view.__class__.__name__, ask_input=False, auto_clear=False)

            choice = choice_text('Are you sure', ['Yes', 'No'])

            if choice == 1:
                add_inv(item_view)
                break
            elif choice == 2:
                continue


def chest(chest_type):
    clear()
    story_text(f'You found a {rarity_text(chest_type, chest_dict[chest_type].rarity)} Chest')

    item = random_option(chest_dict[chest_type].items)

    if type(item) is int:
        story_text(f'+{rarity_text(item, 'gold')} gold')

        player.gold += item

    else:
        story_text(f'+1 {item}')
        item_class = item.__class__.__name__

        if item_class != 'Potion':
            while True:
                inventory('view')
                choice = choice_text(f'Switch {rarity_text(item.name, item.rarity)}?',
                                     ['Yes', 'No', 'View'])

                if choice == 1 and item_class == 'Weapon':
                    if player.weapon == weapon_dict['Fists']:
                        del player.weapon
                    else:
                        add_inv(player.weapon)
                    player.weapon = item
                    break

                elif choice == 1 and item_class == 'Armour':
                    if player.armour == armour_dict['Naked']:
                        del player.armour
                    else:
                        add_inv(player.armour)
                    player.armour = item
                    break

                elif choice == 2:
                    add_inv(item)
                    break

                elif choice == 3:
                    clear()
                    item_subclass = item.__class__.__name__

                    if item_subclass == 'Weapon':
                        view_item(player.weapon, 'Weapon', current=True)
                    elif item_subclass == 'Armour':
                        view_item(player.armour, 'Armour', current=True)

                    print()
                    view_item(item, item_subclass)

                    clear()

        else:
            add_inv(item)
