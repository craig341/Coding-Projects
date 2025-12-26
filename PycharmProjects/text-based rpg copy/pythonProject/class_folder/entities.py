from pythonProject.classes import Entity

from pythonProject.class_folder.equippables.armour import armour_dict
from pythonProject.class_folder.equippables.weapons import weapon_dict

test_dummy = Entity(name='Test Dummy', strength=0, health=100, speed=4, aim=90, max_health=100, gold=0,
                    armour=armour_dict['Naked'], weapon=weapon_dict['Fists'])

goblin = Entity(name='Goblin', strength=1, health=5, speed=2, aim=90, max_health=5, gold=3,
                armour=armour_dict['Naked'], weapon=weapon_dict['Fists'],
                drop_pool={armour_dict['Goblin Armour']: 10})
old_goblin = Entity(name='Old Goblin', strength=1, health=7, speed=2, aim=80, max_health=7, gold=10,
                    armour=armour_dict['Goblin Armour'], weapon=weapon_dict['Cane'])
pixie_goblin = Entity(name='Pixie Goblin', strength=1, health=3, speed=5, aim=90, max_health=3, gold=15,
                      armour=armour_dict['Goblin Armour'], weapon=weapon_dict['Bendy Wand'])
fat_goblin = Entity(name='Fat Goblin', strength=3, health=10, speed=2, aim=80, max_health=10, gold=15,
                    armour=armour_dict['Goblin Armour'], weapon=weapon_dict['Club'])

goblin_troll = Entity(name='Goblin Troll', strength=17, health=20, speed=1, aim=50, max_health=20, gold=20,
                      armour=armour_dict['Trollskin'], weapon=weapon_dict['Club'])
goblin_mage = Entity(name='Goblin Mage', strength=10, health=10, speed=3, aim=90, max_health=10, gold=25,
                     armour=armour_dict['Mage Armour'], weapon=weapon_dict['Goblin Staff'])
goblin_king = Entity(name='Goblin King', strength=20, health=30, speed=2, aim=90, max_health=30, gold=50,
                     armour=armour_dict['Iron Armour'], weapon=weapon_dict['Throwable Goblins'])

koji = Entity(name='Koji', strength=0, health=13, speed=20, aim=20, max_health=13, gold=20,
              armour=armour_dict['Collar Of Koji'], weapon=weapon_dict['Companion Koji'])

enemy_dict = {obj.name: obj for obj in globals().values() if isinstance(obj, Entity)}


def display_entity(entity, total=True):
    print(entity.name)
    print(f'TOTAL STRENGTH: {entity.strength + entity.weapon.damage}' if total else f'STRENGTH: {entity.strength}')
    print(f'HEALTH: {entity.health}/{entity.max_health}')
    print(
        f'TOTAL SPEED: {entity.speed + entity.weapon.speed + entity.armour.speed}' if total else f'SPEED: {entity.speed}')
    print(
        f'TOTAL AIM: {entity.aim + entity.weapon.aim + entity.armour.aim}' if total else f'STRENGTH: {entity.strength}')
    print(f'GOLD: {entity.gold}')
    print(f'WEAPON: {entity.weapon}')
    print(f'ARMOUR: {entity.armour}')


from pythonProject.initial_variables import player

display_entity(player)
print()
display_entity(test_dummy)
# display_enemy(old_goblin)
# display_enemy(pixie_goblin)
# display_enemy(fat_goblin)
# display_entity(goblin_troll)
# display_entity(goblin_mage)
# display_entity(goblin_king)
