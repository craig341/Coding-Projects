from pythonProject.useful_functions.chance_functions import randomise_variable

from pythonProject.class_folder.equippables.weapons import weapon_dict
from pythonProject.class_folder.equippables.armour import armour_dict
from pythonProject.class_folder.equippables.potions import potion_dict

from pythonProject.classes import Chest

starter = Chest(name='Starter', rarity='common',
                items={
                    weapon_dict['Stick']: 25,
                    weapon_dict['Magic Stick']: 25,
                    weapon_dict['Gloves']: 25,
                    weapon_dict['Thick Stick']: 25
                }
                )

Wooden = Chest(name='Wooden', rarity='common',
               items={
                   weapon_dict['Bendy Wand']: 5,
                   weapon_dict['Wooden Sword']: 10,
                   potion_dict['Small Health Potion']: 26,
                   armour_dict['Wooden Armour']: 7,
                   weapon_dict['Club']: 1,
                   weapon_dict['Dagger']: 1,
                   randomise_variable(5): 50
               }
               )

small_potion = Chest(name='Small Potion', rarity='uncommon',
                     items={
                         potion_dict['Small Health Potion']: 40,
                         potion_dict['Small Strength Potion']: 25,
                         potion_dict['Small Speed Potion']: 10,
                         potion_dict['Small Accuracy Potion']: 20,
                         potion_dict['Small Mixed Potion']: 5
                     }
                     )

iron = Chest(name='Iron', rarity='rare',
             items={
                 armour_dict['Iron Armour']: 25,
                 weapon_dict['Iron Sword']: 25,
                 potion_dict['Small Speed Potion']: 20,
                 potion_dict['Mixed Potion']: 10,
                 randomise_variable(10): 20
             }
             )

gold = Chest(name='Gold', rarity='epic',
             items={
                 weapon_dict['Lance']: 20,
                 weapon_dict['War Axe']: 5,
                 weapon_dict['Gold Sword']: 20,
                 weapon_dict['Blood Sword']: 5,
                 armour_dict['Rhino Armour']: 5,
                 armour_dict['Gold Armour']: 20,
                 potion_dict['Strong Health Potion']: 15,
                 potion_dict['Holy Water']: 10,
                 potion_dict['God Piss']: 1
             }
             )

chest_dict = {obj.name: obj for obj in globals().values() if isinstance(obj, Chest)}



print('hello world'.title())