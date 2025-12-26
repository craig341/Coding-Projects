class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Weapon(Item):
    def __init__(self, name, price, damage=0, speed=3):
        super().__init__(name, price)
        self.damage = damage
        self.speed = speed


class Armour(Item):
    def __init__(self, name, price, defense=0):
        super().__init__(name, price)
        self.defense = defense


fists = Weapon(name='Fists', price=0, damage=1, speed=3)
iron_dagger = Weapon(name='Iron Dagger', price=5, damage=3, speed=4)
iron_sword = Weapon(name='Iron Sword', price=10, damage=5, speed=3)
iron_spear = Weapon(name='Iron Spear', price=12, damage=10, speed=2)

naked = Armour(name='Naked', price=0, defense=0)
normal_clothes = Armour(name='Normal Clothes', price=1, defense=1)
iron_armour = Armour(name='Iron Armour', price=20, defense=10)


