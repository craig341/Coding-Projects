from classes import Armour
# name price defence speed rarity

naked = Armour(name='Naked', price=0, defence=0, speed=-1, rarity='common')
clothes = Armour(name='Clothes', price=1, defence=1, speed=0, rarity='common')
goblin_armour = Armour(name='Goblin Armour', price=3, defence=2, speed=0, rarity='common')
leafy_armour = Armour(name='Leafy Armour', price=3, defence=2, speed=0, rarity='common')

wooden_armour = Armour(name='Wooden Armour', price=9, defence=3, speed=-1, rarity='uncommon')
chainmail_armour = Armour(name='Chainmail Armour', price=15, defence=3, speed=1, rarity='uncommon')

iron_armour = Armour(name='Iron Armour', price=20, defence=5, speed=-1, rarity='rare')

gold_armour = Armour(name='Gold Armour', price=37, defence=9, speed=-1, rarity='epic')
rhino_armour = Armour(name='Rhino Armour', price=52, defence=10, speed=1, rarity='epic')
knight_armour = Armour(name='Knight Armour', price=34, defence=8, speed=-1, rarity='epic')
titanium_armour = Armour(name='Titanium Armour', price=45, defence=14, speed=-2, rarity='epic')

dragon_scale_armour = Armour(name='Dragon Scale Armour', price=104, defence=18, speed=1, rarity='legendary')
fallen_king_armour = Armour(name='Fallen King Armour', price=100, defence=20, speed=-1, rarity='legendary')
demon_wings = Armour(name='Demon Wings', price=130, defence=13, speed=7, rarity='legendary')

true_king_armour = Armour(name='True King Armour', price=1000, defence=50, speed=2, rarity='ancient')

armour_dict = {obj.name: obj for obj in globals().values() if isinstance(obj, Armour)}

