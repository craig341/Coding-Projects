from pythonProject.classes import Weapon

# name price damage speed aim crit rarity

fists = Weapon(name='Fists', description='go fist him', price=0, damage=1, speed=0, aim=0, durability=-1, rarity='common')
stick = Weapon(name='Stick', price=1, damage=3, speed=0, aim=0, rarity='common')
magic_stick = Weapon(name='Magic Stick', price=3, damage=2, speed=0, aim=3, rarity='common')
gloves = Weapon(name='Gloves', price=1, damage=1, speed=2, aim=1, rarity='common')
thick_stick = Weapon(name='Thick Stick', price=1, damage=5, speed=-2, aim=-7, rarity='common')
cane = Weapon(name='Cane', price=3, damage=2, speed=0, aim=-5, rarity='common')
plunger = Weapon(name='Plunge', price=4, damage=2, speed=0, aim=0, crit_chance=-2, rarity='common')

bendy_wand = Weapon(name='Bendy Wand', price=8, damage=5, speed=0, aim=3, rarity='uncommon')
wooden_sword = Weapon(name='Wooden Sword', price=6, damage=4, speed=0, aim=0, rarity='uncommon')
leaf_blade = Weapon(name='Leaf Blade', price=10, damage=5, speed=1, aim=0, rarity='uncommon')

slingshot = Weapon(name='Slingshot', price=15, damage=5, aim=20, speed=1, rarity='rare')
club = Weapon(name='Club', price=20, damage=8, speed=-1, aim=-20, rarity='rare')
dagger = Weapon(name='Dagger', price=10, damage=3, speed=2, aim=7, rarity='rare')
iron_sword = Weapon(name='Iron Sword', price=24, damage=7, speed=1, aim=0, rarity='rare')
lance = Weapon(name='Lance', price=30, damage=9, speed=-1, aim=10, rarity='rare')
iron_hammer = Weapon(name='Iron Hammer', price=25, damage=8, speed=-1, aim=-10, rarity='rare')
goblin_staff = Weapon(name='Goblin Staff', price=17, damage=5, speed=0, aim=10, rarity='rare')
needle = Weapon(name='Needle', price=23, damage=10, speed=0, aim=-10, crit_chance=5, rarity='rare')

gold_sword = Weapon(name='Gold Sword', price=46, damage=12, speed=1, aim=0, rarity='epic')
war_axe = Weapon(name='War Axe', price=46, damage=18, speed=-1, aim=-5, rarity='epic')
knight_blade = Weapon(name="Knight Blade", price=50, damage=15, speed=1, aim=5, rarity='epic')
blood_sword = Weapon(name='Blood Sword', price=30, damage=10, speed=0, aim=0, rarity='epic')
throwable_goblins = Weapon(name='Throwable Goblins', price=40, damage=15, speed=1, aim=5, rarity='epic')

warrior_hammer = Weapon(name="Warrior Hammer", price=98, damage=25, speed=-1, rarity='legendary')
dragon_staff = Weapon(name='Dragon Staff', price=112, damage=27, speed=2, aim=5, rarity='legendary')
koji_pet = Weapon(name='Companion Koji', price=2000, damage=30, speed=5, aim=0, rarity='legendary')

devil_blade = Weapon(name='Devil Blade', description='dealt with the devil', price=666, damage=200, speed=1, aim=10, crit_chance=30, rarity='ancient')

hurt_stick = Weapon(name='hurt stick', price=999, damage=999999999999999999999999, speed=999, aim=100, durability=-1, rarity='developer')

weapon_dict = {obj.name: obj for obj in globals().values() if isinstance(obj, Weapon)}
