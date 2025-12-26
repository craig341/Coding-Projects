from pythonProject.classes import Entity

from pythonProject.class_folder.equippables.armour import armour_dict
from pythonProject.class_folder.equippables.weapons import weapon_dict

inv = {}
developer = False
player = Entity(armour=armour_dict['Clothes'], weapon=weapon_dict['Fists'], strength=1, health=20, max_health=20,
                speed=4, aim=95, crit_chance=0, crit_multiplier=2)


def set_developer_status(status):
    developer['status'] = status
    return developer
