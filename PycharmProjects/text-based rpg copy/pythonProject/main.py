from pythonProject.levels.goblin_forest import level_1

from pythonProject.initial_variables import player
import initial_variables

from pythonProject.useful_functions.inventory_functions import add_inv
from pythonProject.useful_functions.print_functions import text_boundary, clear, rarity_text

from pythonProject.class_folder.equippables.weapons import weapon_dict


def developer_on():
    initial_variables.developer = True


def main():
    name = ''

    while not name:
        clear()
        text_boundary('start')
        print('Name your character: ')
        text_boundary('end')
        name = input().upper()

    if name in ['DEVELOPER', 'CHEATS']:
        add_inv(weapon_dict['hurt stick'])
        developer_on()

        print(rarity_text('CHEATS ON', 'special'))
        input()

    player.name = name
    clear()

    level_1()


if __name__ == '__main__':
    main()
