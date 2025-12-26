from pythonProject.levels.goblin_forest import goblin_forest
from pythonProject.levels.latin_revision.latin_revision_level import latin_revision

from pythonProject.initial_variables import player
import pythonProject.initial_variables

from pythonProject.useful_functions.inventory_functions import add_inv
from pythonProject.useful_functions.print_functions import text_boundary, clear, rarity_text

from pythonProject.class_folder.equippables.weapons import weapon_dict
from pythonProject.class_folder.equippables.relics import relic_dict


def developer_on():
    pythonProject.initial_variables.developer = True


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
        add_inv(relic_dict['Developer Pass'])
        developer_on()

        print(rarity_text('CHEATS ON', 'developer'))
        input()

    player.name = name
    clear()

    # latin_revision()

    goblin_forest()


if __name__ == '__main__':
    main()
