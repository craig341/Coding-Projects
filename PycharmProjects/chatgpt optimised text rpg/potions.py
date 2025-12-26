from classes import Potion

# name price attribute changes duration rarity
# attributes: [strength, health, speed, aim]

small_strength_potion = Potion(name='Small Strength Potion', price=2, attribute_changes=[2, 0, 0, 0], duration=2,
                               rarity='common')
small_hp_potion = Potion(name='Small HP Potion', price=2, attribute_changes=[0, 5, 0, 0], duration=0,
                             rarity='common')
small_speed_potion = Potion(name='Small Speed Potion', price=2, attribute_changes=[0, 0, 1, 0], duration=2,
                            rarity='common')
small_accuracy_potion = Potion(name='Small Accuracy Potion', price=2, attribute_changes=[0, 0, 0, 2], duration=2,
                               rarity='common')
small_mixed_potion = Potion(name='Small Mixed Potion', price=5, attribute_changes=[1, 3, 1, 1], duration=3,
                            rarity='common')
bread = Potion(name='Bread', price=2, attribute_changes=[1, 2, 0, 0], duration=2, rarity='common')

hp_potion = Potion(name='HP Potion', price=5, attribute_changes=[0, 10, 0, 0], duration=0, rarity='uncommon')
mixed_potion = Potion(name='Mixed Potion', price=8, attribute_changes=[2, 5, 1, 2], duration=3, rarity='uncommon')
strength_potion = Potion(name='Strength Potion', price=4, attribute_changes=[4, 0, 0, 0], duration=2, rarity='uncommon')
speed_potion = Potion(name='Speed Potion', price=6, attribute_changes=[0, 0, 2, 0], duration=4, rarity='uncommon')
accuracy_potion = Potion(name='Accuracy Potion', price=4, attribute_changes=[0, 0, 0, 5], duration=2, rarity='uncommon')
cake = Potion(name='Cake', price=7, attribute_changes=[1, 0, 2, 0], duration=5, rarity='uncommon')

strong_hp_potion = Potion(name='Strong HP Potion', price=12, attribute_changes=[0, 20, 0, 0], duration=0, rarity='rare')

pure_hp_potion = Potion(name='Pure HP Potion', price=25, attribute_changes=[0, 40, 0, 0], duration=0, rarity='epic')
holy_water = Potion(name='Holy Water', price=30, attribute_changes=[5, 10, 2, 10], duration=3, rarity='epic')
cocaine = Potion(name='Cocaine', price=43, attribute_changes=[7, -4, 2, -20], duration=3)


full_hp_potion = Potion(name='Full HP Potion', price=75, attribute_changes=[0, 10000, 0, 0], duration=0, rarity='legendary')
god_piss = Potion(name='God Piss', price=100, attribute_changes=[7, 20, 1, 10], duration=5, rarity='legendary')
devil_ether = Potion(name='Devil Ether', price=66, attribute_changes=[100, -5, 0, 50], duration=0)


potion_dict = {obj.name: obj for obj in globals().values() if isinstance(obj, Potion)}
