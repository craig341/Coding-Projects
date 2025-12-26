from classes import Entity
from armour import armour_dict
from weapons import weapon_dict


goblin = Entity(name='Goblin', strength=1, health=5, speed=3, aim=90, max_health=5, gold=3,
                armour=armour_dict['Naked'], weapon=weapon_dict['Fists'])
old_goblin = Entity(name='Old Goblin', strength=1, health=7, speed=2, aim=80, max_health=7, gold=10,
                    armour=armour_dict['Goblin Armour'], weapon=weapon_dict['Fists'])
pixie_goblin = Entity(name='Pixie Goblin', strength=1, health=3, speed=5, aim=90, max_health=3, gold=15,
                      armour=armour_dict['Goblin Armour'], weapon=weapon_dict['Bendy Wand'])
fat_goblin = Entity(name='Fat Goblin', strength=5, health=10, speed=1, aim=60, max_health=10, gold=15,
                    armour=armour_dict['Goblin Armour'], weapon=weapon_dict['Fists'])

goblin_troll = Entity(name='Goblin Troll', strength=17, health=20, speed=1, aim=50, max_health=15, gold=20)
goblin_mage = Entity(name='Goblin Mage', strength=10, health=10, speed=3, aim=90, max_health=10, gold=25)
goblin_king = Entity(name='Goblin King', strength=20, health=30, speed=2, aim=90, max_health=30, gold=50)


enemy_dict = {obj.name: obj for obj in globals().values() if isinstance(obj, Entity)}
