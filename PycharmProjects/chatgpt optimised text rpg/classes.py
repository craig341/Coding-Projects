from colorama import Fore, Style
from chance_functions import randomise_variable

rarity_dict = {
    'default': Style.RESET_ALL,
    'common': Fore.WHITE,
    'uncommon': Fore.GREEN,
    'rare': Fore.BLUE,
    'epic': Fore.MAGENTA,
    'legendary': Fore.LIGHTYELLOW_EX,
    'ancient': Fore.LIGHTRED_EX,
    'special': Fore.LIGHTCYAN_EX,
    'gold': Fore.YELLOW,
    'bleed': Fore.RED,
    'black': Fore.BLACK,
    'red': Fore.RED,
    'bright_green': Fore.LIGHTGREEN_EX,
    'bright_blue': Fore.LIGHTBLUE_EX,
    'bright_magenta': Fore.LIGHTMAGENTA_EX,
    'bright_white': Fore.LIGHTWHITE_EX,
    'cyan': Fore.CYAN,
    'dim': Style.DIM,
    'bright': Style.BRIGHT,
}


def rarity_text(text: str, rarity: str) -> str:
    return f"{rarity_dict[rarity]}{text}{rarity_dict['default']}"


class Item:
    def __init__(self, name: str, price: int, rarity='default'):
        self.name = name
        self.price = price
        self.rarity = rarity

    def __str__(self):
        return f"{rarity_text(self.name, self.rarity)}"


class Weapon(Item):
    def __init__(self, name, price, damage, speed=0, aim=0, bleed=None, stun=None, confuse=None, rarity='default'):
        super().__init__(name, price, rarity)
        self.damage = damage
        self.speed = speed
        self.aim = aim
        self.bleed = bleed or []
        self.stun = stun or []
        self.confuse = confuse or []


class Armour(Item):
    def __init__(self, name, price, defence, speed, rarity='default'):
        super().__init__(name, price, rarity)
        self.defence = defence
        self.speed = speed


class Potion(Item):
    def __init__(self, name, price, attribute_changes, duration=0, rarity='default', cooldown=False):
        super().__init__(name, price, rarity)
        self.attribute_changes = attribute_changes
        self.duration = duration
        self.cooldown = cooldown


class Entity:
    def __init__(self, name='Unnamed', strength=1, health=20, speed=3, aim=90, max_health=20, weapon=None, armour=None,
                 gold=0):
        self.name = name
        self.strength = strength
        self.health = health
        self.speed = speed
        self.max_health = max_health
        self.weapon = weapon or Weapon("Fists", 0, 1)
        self.armour = armour or Armour("Clothes", 0, 0, 0)
        self.gold = gold
        self.aim = aim

    def attack(self, target):
        base_damage = self.strength + self.weapon.damage
        randomized_damage = randomise_variable(base_damage)
        damage_dealt = max(randomized_damage - target.armour.defence, 0)
        target.health = max(target.health - damage_dealt, 0)
        return damage_dealt


class Shop:
    def __init__(self, name, items, rest_price=0):
        self.name = name
        self.items = items
        self.rest_price = rest_price


class Merchant:
    def __init__(self, name, bias):
        self.name = name
        self.bias = bias
