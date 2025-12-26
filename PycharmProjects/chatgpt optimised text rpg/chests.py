import random

from chance_functions import randomise_variable
from weapons import weapon_dict
from armour import armour_dict
from potions import potion_dict


chest_rarity_dict = {
        'Starter': 'common',
        'Wooden': 'common',

        'Small Potion': 'uncommon',

        'Iron': 'rare',

        'Gold': 'epic',
    }

chest_dict = {
    'Starter': [
        (weapon_dict['Stick'], 25),
        (weapon_dict['Magic Stick'], 25),
        (weapon_dict['Gloves'], 25),
        (weapon_dict['Thick Stick'], 25)
    ],

    'Wooden': [
        (weapon_dict['Bendy Wand'], 5),
        (weapon_dict['Wooden Sword'], 10),
        (potion_dict['Small HP Potion'], 26),
        (armour_dict['Wooden Armour'], 7),
        (weapon_dict['Club'], 1),
        (weapon_dict['Dagger'], 1),
        (randomise_variable(5), 50),
    ],

    'Small Potion': [
        (potion_dict['Small HP Potion'], 40),
        (potion_dict['Small Strength Potion'], 25),
        (potion_dict['Small Speed Potion'], 10),
        (potion_dict['Small Accuracy Potion'], 20),
        (potion_dict['Small Mixed Potion'], 5),
    ],

    'Iron': [
        (armour_dict['Iron Armour'], 25),
        (weapon_dict['Iron Sword'], 25),
        (potion_dict['Small Speed Potion'], 20),
        (potion_dict['Mixed Potion'], 10),
        (randomise_variable(10), 20),
    ],

    'Gold': [
            (weapon_dict['Lance'], 20),
            (weapon_dict['War Axe'], 5),
            (weapon_dict['Gold Sword'], 20),
            (weapon_dict['Blood Sword'], 5),
            (armour_dict['Rhino Armour'], 5),
            (armour_dict['Gold Armour'], 20),
            (potion_dict['Strong HP Potion'], 15),
            (potion_dict['Holy Water'], 10),
            (potion_dict['God Piss'], 1),

        ]
}