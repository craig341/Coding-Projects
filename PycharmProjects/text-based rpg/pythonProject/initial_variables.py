from pythonProject.classes import Entity

from pythonProject.class_folder.equippables.armour import armour_dict
from pythonProject.class_folder.equippables.weapons import weapon_dict
from pythonProject.class_folder.equippables.relics import relic_dict

inv = {}
player = Entity(armour=armour_dict['Clothes'], weapon=weapon_dict['Fists'], relic=relic_dict['None'], strength=3, health=20, max_health=20,
                speed=4, aim=95, crit_chance=0, crit_multiplier=2)
