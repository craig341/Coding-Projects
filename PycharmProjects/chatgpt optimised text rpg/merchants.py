from classes import Merchant


def bias_dict(weapon_bias=1.0, armour_bias=1.0, potion_bias=1.0, set_all=1.0):
    return {
        'Weapon': weapon_bias if weapon_bias != 1 else set_all,
        'Armour': armour_bias if armour_bias != 1 else set_all,
        'Potion': potion_bias if potion_bias != 1 else set_all
    }


blacksmith_merchant = Merchant('Blacksmith', bias_dict(weapon_bias=1.5, armour_bias=1.5, potion_bias=0.5))
alchemist_merchant = Merchant('Alchemist', bias_dict(set_all=0.3, potion_bias=2))
rich_duke = Merchant('Rich Duke', bias_dict(set_all=1.4))
knight = Merchant('Knight', bias_dict(weapon_bias=1.8, armour_bias=1.2, potion_bias=1.2))


merchant_dict = {obj.name: obj for obj in globals().values() if isinstance(obj, Merchant)}
