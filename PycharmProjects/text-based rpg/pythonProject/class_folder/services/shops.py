from pythonProject.class_folder.equippables.weapons import weapon_dict
from pythonProject.class_folder.equippables.armour import armour_dict
from pythonProject.class_folder.equippables.potions import potion_dict

from pythonProject.classes import Shop


village_shop = Shop(name='Village Shop',
                    items=[
                        [weapon_dict['Bendy Wand'], 2],
                        [weapon_dict['Wooden Sword'], 3],
                        [weapon_dict['Leaf Blade'], 1],
                        [armour_dict['Leafy Armour'], 3],
                        [weapon_dict['Slingshot'], 1],
                        [potion_dict['Small Health Potion'], 6],
                        [potion_dict['Small Strength Potion'], 3],
                        [potion_dict['Health Potion'], 4],
                    ],
                    rest=[5, 7]
                    )

blacksmith_shop = Shop(name='Blacksmith Shop',
                       items=[
                           [weapon_dict['Dagger'], 2],
                           [weapon_dict['Iron Hammer'], 4],
                           [armour_dict['Chainmail Armour'], 2],
                           [armour_dict['Iron Armour'], 3],
                           [weapon_dict['Iron Sword'], 4],
                           [weapon_dict['Lance'], 1],
                           [armour_dict['Knight Armour'], 1],
                       ],
                       )

knight_outpost = Shop(name='Knight Outpost',
                      items=[
                          [weapon_dict['Iron Sword'], 2],
                          [weapon_dict['Lance'], 2],
                          [weapon_dict['War Axe'], 1],
                          [weapon_dict['Knight Blade'], 1],
                          [armour_dict['Iron Armour'], 3],
                          [armour_dict['Knight Armour'], 2],
                          [armour_dict['Titanium Armour'], 1],
                          [armour_dict['Fallen King Armour'], 1],

                      ],
                      )

medicine_dealer = Shop(name='Medicine Dealer',
                       items=[
                           [potion_dict['Small Health Potion'], 5],
                           [potion_dict['Health Potion'], 5],
                           [potion_dict['Strong Health Potion'], 3],
                           [potion_dict['Pure Health Potion'], 1],
                           [potion_dict['Paracetamol'], 3],
                           [potion_dict['EpiPen'], 2],
                           [weapon_dict['Needle'], 1],
                           [potion_dict['Magic Grass'], 1],
                           [potion_dict['Cocaine'], 1],

                       ],

                       )

shop_dict = {obj.name: obj for obj in globals().values() if isinstance(obj, Shop)}

