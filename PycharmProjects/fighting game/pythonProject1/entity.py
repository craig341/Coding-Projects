from item import fists,naked
from healthbar import HealthBar

class Entity:
    def __init__(self, name, health=100, strength=10, speed=3, weapon=fists, armour=naked):
        self.name = name
        self.health = health
        self.max_health = health
        self.strength = strength
        self.speed = speed
        self.weapon = weapon
        self.armour = armour
        self.health_bar = HealthBar(self)

    def attack(self, target):
        total_dmg = self.strength + self.weapon.damage - self.armour.defense
        target.health -= max(total_dmg, 0)
        target.health_bar.update()


weapon_dict = {'none': 0}

armour_dict = {'none': 0}


def weapon_val(weapon):
    return weapon_dict[weapon]


def armour_val(armour):
    return armour_dict[armour]
