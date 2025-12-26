from colorama import Fore, Style

rarity_dict = {'default': Style.RESET_ALL,
               'common': Fore.WHITE,
               'uncommon': Fore.GREEN,
               'rare': Fore.BLUE,
               'epic': Fore.MAGENTA,
               'legendary': Fore.LIGHTYELLOW_EX,
               'ancient': Fore.LIGHTRED_EX,
               'special': Fore.LIGHTCYAN_EX,
               'gold': Fore.YELLOW,

               'bleed': Fore.RED,
               'crit': Fore.LIGHTMAGENTA_EX,

               'black': Fore.BLACK,  # New
               'red': Fore.RED,  # New
               'bright_green': Fore.LIGHTGREEN_EX,  # New
               'bright_blue': Fore.LIGHTBLUE_EX,  # New
               'bright_magenta': Fore.LIGHTMAGENTA_EX,  # New
               'bright_white': Fore.LIGHTWHITE_EX,  # New
               'cyan': Fore.CYAN,  # New
               'dim': Style.DIM,  # Styling
               'bright': Style.BRIGHT,
               }


# for rarity, color in rarity_dict.items():
#     print(f"{color}{rarity.capitalize()}{Style.RESET_ALL}")


class Item:
    def __init__(self, name='no name', description='no description', price=0,
                 item_type='no item type', origin='no origin', rarity='default'):

        self.name = name
        self.description = description
        self.price = price
        self.item_type = item_type
        self.origin = origin
        self.rarity = rarity

    def __str__(self):
        colour = rarity_dict.get(self.rarity)
        return f"{colour}{self.name}{Style.RESET_ALL}"


class Weapon(Item):
    def __init__(self, name='no name', description='no description', price=0,
                 damage=0, speed=0, aim=0, crit_chance=0, crit_multiplier=2, durability=-1,
                 item_type='no item type', origin='no origin', rarity='default'):

        super().__init__(name, description, price, item_type, origin, rarity)
        self.damage = damage
        self.speed = speed
        self.aim = aim
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.durability = durability


class Armour(Item):
    def __init__(self, name='no name', description='no description', price=0,
                 defence=0, speed=0, aim=0, crit_chance=0,  crit_multiplier=2, durability=-1,
                 item_type='no item type', origin='no origin', rarity='default'):

        super().__init__(name, description, price, item_type, origin, rarity)
        self.defense = defence
        self.speed = speed
        self.aim = aim
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.durability = durability


class Potion(Item):
    def __init__(self, name='no name', description='no description', price=0,
                 attribute_changes=None, duration=1,
                 item_type='no item type', origin='no origin', rarity='default'):

        super().__init__(name, description, price, item_type, origin, rarity)
        if attribute_changes is None:
            attribute_changes = [0, 0, 0, 0]
        self.attribute_changes = attribute_changes
        self.duration = duration


class Entity:
    def __init__(self, name='no name', strength=0, health=1, speed=0, aim=0, crit_chance=10, crit_multiplier=2, max_health=1, weapon=None, armour=None, drop_pool=None, gold=0):
        self.name = name
        self.strength = strength
        self.health = health
        self.speed = speed
        self.aim = aim
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.max_health = max_health
        self.weapon = weapon
        self.armour = armour
        self.drop_pool = drop_pool if drop_pool is not None else {}
        self.gold = gold


class Shop:
    def __init__(self, name, items, rest=0):
        self.name = name
        self.items = items
        self.rest = rest  # [rest_price, rest health restored]


class Merchant:
    def __init__(self, name, bias):
        self.name = name
        self.bias = bias


class Chest:
    def __init__(self, name, items, rarity):
        self.name = name
        self.items = items
        self.rarity = rarity
