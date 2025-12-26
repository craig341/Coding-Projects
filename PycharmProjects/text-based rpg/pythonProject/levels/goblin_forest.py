import random

from pythonProject.useful_functions.print_functions import clear, story_text
from pythonProject.useful_functions.chance_functions import random_option, simple_chance

from pythonProject.class_folder.entities import enemy_dict

from pythonProject.class_folder.services.shops import shop_dict

from pythonProject.events.fight_event import fight
from pythonProject.events.shop_event import shop
from pythonProject.events.merchant_event import merchant
from pythonProject.events.boss_event import boss


def goblin_forest():
    story_text('You wake up in a forest...')

    # fight(enemy_dict['Test Dummy'])
    fight(enemy_dict['Goblin'], 100, 'Starter')
    clear()

    for i in range(random.randint(3, 5)):
        fight(random_option(
            {enemy_dict['Goblin']: 90,
             enemy_dict['Fat Goblin']: 1,
             enemy_dict['Old Goblin']: 9}),
            80, ('Wooden' if simple_chance(60) else 'Small Potion'))

    shop('Village Shop')

    for i in range(random.randint(9, 15)):
        fight(random_option(
            {enemy_dict['Goblin']: 50,
             enemy_dict['Fat Goblin']: 10,
             enemy_dict['Old Goblin']: 20,
             enemy_dict['Pixie Goblin']: 20}
        ),
            70, ('Wooden' if simple_chance(80) else 'Iron'))
        if simple_chance(20):
            (shop('Village Shop') if simple_chance(60) else shop('Blacksmith Shop'))

        if simple_chance(30):
            merchant(random_option(
                {'Blacksmith': 40,
                 'Alchemist': 40,
                 'Rich Duke': 10,
                 'Knight': 10, }
            ))

    boss()

    for i in range(random.randint(9, 15)):
        fight(random_option(
            {enemy_dict['Fat Goblin']: 30,
             enemy_dict['Old Goblin']: 20,
             enemy_dict['Pixie Goblin']: 20}
        ),
            70, ('Wooden' if simple_chance(80) else 'Iron'))

        if simple_chance(20):
            # shop(random_option(
            #     {shop_dict['Village Shop']: 55,
            #      shop_dict['Blacksmith Shop']: 40,
            #      shop_dict['Medicine Dealer']: 5,
            #      }
            # ))

            shop(random_option(
                {'Village Shop': 55,
                 'Blacksmith Shop': 40,
                 'Medicine Dealer': 5,
                 }
            ))

        if simple_chance(30):
            merchant(random_option(
                {'Blacksmith': 40,
                 'Alchemist': 40,
                 'Rich Duke': 10,
                 'Knight': 10, }
            ))

    for i in range(random.randint(9, 15)):
        fight(random_option(
            {enemy_dict['Fat Goblin']: 30,
             enemy_dict['Old Goblin']: 30,
             enemy_dict['Pixie Goblin']: 30,
             enemy_dict['Goblin Troll']: 5,
             enemy_dict['Goblin Mage']: 4,
             enemy_dict['Goblin King']: 1,
             }
        ),
            70, ('Iron' if simple_chance(80) else 'Gold'))

        if simple_chance(20):
            shop(random_option(
                {'Village Shop': 40,
                 'Blacksmith Shop': 40,
                 'Knight Outpost': 10,
                 'Medicine Dealer': 10,
                 }
            ))

        if simple_chance(30):
            merchant(random_option(
                {'Blacksmith': 30,
                 'Alchemist': 30,
                 'Rich Duke': 20,
                 'Knight': 20, }
            ))

    while True:
        fight(random_option(
            {enemy_dict['Fat Goblin']: 30,
             enemy_dict['Pixie Goblin']: 20,
             enemy_dict['Goblin Troll']: 30,
             enemy_dict['Goblin Mage']: 20,
             enemy_dict['Goblin King']: 1,
             }
        ),
            60, ('Iron' if simple_chance(70) else 'Gold'))

        if simple_chance(20):
            shop(random_option(
                {'Village Shop': 20,
                 'Blacksmith Shop': 30,
                 'Knight Outpost': 20,
                 'Medicine Dealer': 30,
                 }
            ))

        if simple_chance(30):
            merchant(random_option(
                {'Blacksmith': 30,
                 'Alchemist': 30,
                 'Rich Duke': 20,
                 'Knight': 20, }
            ))
