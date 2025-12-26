from colorama import Fore, Style

rarity_dict = {
    'default': '\033[0m',
    'common': '\033[38;5;240m',
    'uncommon': '\033[38;5;70m',
    'rare': '\033[38;5;39m',
    'epic': '\033[38;5;99m',
    'legendary': '\033[38;5;184m',
    'ancient': '\033[38;5;160m',
    'gold': '\033[38;5;3m',

    'bleed': '\033[38;5;88m',
    'crit': '\033[38;5;207m',

    'player': '\033[38;5;10m',
    'enemy': '\033[38;5;9m',
    'developer': '\033[38;5;87m',

}

# for rarity, color in rarity_dict.items():
#     print(f"{color}{rarity.capitalize()}{Style.RESET_ALL}")
# input()


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
                 defence=0, speed=0, aim=0, crit_chance=0, crit_multiplier=2, durability=-1,
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


class Relic(Item):
    def __init__(self, name='no name', description='no description', price=0,
                 strength=0, speed=0, aim=0, crit_chance=10, crit_multiplier=2, defence=0, effects=None,
                 item_type='no item type', origin='no origin', rarity='default'):
        super().__init__(name, description, price, item_type, origin, rarity)
        self.strength = strength
        self.speed = speed
        self.aim = aim
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.defence = defence
        self.effects = effects if effects is not None else {}


class Entity:
    from pythonProject.class_folder.equippables.relics import none as none_relic

    def __init__(self, name='no name', strength=0, health=1, speed=0, aim=0, crit_chance=10, crit_multiplier=2,
                 max_health=1, weapon=None, armour=None, relic=none_relic, drop_pool=None, gold=0):
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
        self.relic = relic
        self.drop_pool = drop_pool if drop_pool is not None else {}
        self.gold = gold

    def view_enemy(self, ask_input=False):
        print('NAME:', self.name)
        print('WEAPON:', self.weapon)
        print('ARMOUR:', self.armour)
        print('RELIC:', self.relic)
        print('GOLD:', self.gold)
        print('DROP POOL:')
        for key, value in self.drop_pool.items():
            print(f"\t{key}, Chance: {value}")
        print()
        print('TOTAL STRENGTH:', self.strength + self.weapon.damage + self.relic.strength)
        print('TOTAL DEFENCE:', self.armour.defense + self.relic.defence)
        print('TOTAL SPEED:', self.speed + self.weapon.speed + self.armour.speed + self.relic.speed)
        print('TOTAL AIM:', self.aim + self.weapon.aim + self.armour.aim + self.relic.aim)
        print('CRIT CHANCE:', self.crit_chance + self.weapon.crit_chance + self.armour.crit_chance + self.relic.crit_chance)
        print('CRIT MULTIPLIER:', round((self.crit_multiplier + self.weapon.crit_multiplier + self.armour.crit_multiplier + self.relic.crit_multiplier) / 4, 1))
        print('HEALTH:', self.max_health)

        if ask_input:
            input()



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
