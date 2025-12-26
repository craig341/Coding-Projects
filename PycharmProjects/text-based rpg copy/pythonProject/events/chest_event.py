from pythonProject.useful_functions.print_functions import clear, story_text, rarity_text, choice_text, view_item
from pythonProject.useful_functions.chance_functions import random_option
from pythonProject.useful_functions.inventory_functions import inventory, add_inv

from pythonProject.class_folder.equippables.weapons import weapon_dict
from pythonProject.class_folder.equippables.armour import armour_dict

from pythonProject.class_folder.services.chests import chest_dict

from pythonProject.initial_variables import player


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
            choice_made = False
            while not choice_made:

                inventory('view')
                choice = choice_text(f'Switch {rarity_text(item.name, item.rarity)}?',
                                     ['Yes', 'No', 'View'])

                if choice == 1 and item_class == 'Weapon':
                    if player.weapon == weapon_dict['Fists']:
                        del player.weapon
                    else:
                        add_inv(player.weapon)
                    player.weapon = item
                    choice_made = True

                elif choice == 1 and item_class == 'Armour':
                    if player.armour == armour_dict['Naked']:
                        del player.armour
                    else:
                        add_inv(player.armour)
                    player.armour = item
                    choice_made = True

                elif choice == 2:
                    add_inv(item)
                    choice_made = True

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
        else:
            add_inv(item)
