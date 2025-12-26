import random
from classes import Entity, rarity_text
from print_functions import healthbar, story_text, text_boundary, clear, choice_text, death
from chance_functions import simple_chance, random_option, randomise_variable

from armour import armour_dict
from weapons import weapon_dict
from potions import potion_dict
from enemies import enemy_dict
from shops import shop_dict
from merchants import merchant_dict
from chests import chest_rarity_dict, chest_dict

# Global inventory and player setup
inventory = {}
player = Entity(name="Hero", armour=armour_dict['Clothes'], weapon=weapon_dict['Fists'], health=20, speed=3, aim=95)


def add_to_inventory(item, quantity=1):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity


def remove_from_inventory(item, quantity=1):
    if item in inventory:
        inventory[item] -= quantity
        if inventory[item] <= 0:
            del inventory[item]


def display_inventory(mode="view"):
    text_boundary()
    print(f"{rarity_text('GOLD', 'gold')}: {player.gold}")
    print(f"WEAPON: {player.weapon}")
    print(f"ARMOUR: {player.armour}")
    for idx, (item, count) in enumerate(inventory.items(), start=1):
        item_display = f"{item} x{count}" if count > 1 else str(item)
        print(f"{idx}. {item_display}")
    text_boundary()

    if mode == "use":
        try:
            choice = int(input("Choose an item by number (-1 to cancel): "))
            if choice == -1:
                return None
            return list(inventory.keys())[choice - 1]
        except (ValueError, IndexError):
            return None


def fight(enemy, chest_chance=0, chest_type=None):
    """Simulate a fight with an enemy."""

    def update_stats():
        player.speed += player.armour.speed + player.weapon.speed
        player.aim = min(player.aim + player.weapon.aim, 99)
        enemy.speed += enemy.armour.speed + enemy.weapon.speed
        enemy.aim = min(enemy.aim + enemy.weapon.aim, 99)

    def fight_ui():
        clear()
        text_boundary()
        healthbar(player)
        print()
        healthbar(enemy, player=False)
        text_boundary()

    def attack(attacker, defender):
        if not simple_chance(attacker.aim):
            fight_ui()
            print(f"{attacker.name} missed!")
        else:
            damage = attacker.attack(defender)
            fight_ui()
            print(f"{attacker.name} dealt {damage} damage!")
            if defender.health <= 0:
                return True
        input()
        return False

    update_stats()
    story_text(f"You encounter a {enemy.name}!")

    turn_order = "player" if player.speed >= enemy.speed else "enemy"
    potion_cooldowns = {}

    while player.health > 0 and enemy.health > 0:
        fight_ui()
        if turn_order == "player":
            choice = choice_text("What will you do?", ["Attack", "Use Item", "Run"])
            if choice == 1:
                if attack(player, enemy):
                    print(f"{enemy.name} has been defeated!")
                    loot = randomise_variable(enemy.gold)
                    player.gold += loot
                    print(f"You gained {rarity_text(loot, 'gold')} gold!")
                    break
            elif choice == 2:
                item = display_inventory(mode="use")
                if item and item.__class__.__name__ == "Potion":
                    # Apply potion effects here
                    pass
            elif choice == 3:
                if simple_chance(player.speed / (player.speed + enemy.speed) * 100):
                    print("You successfully fled!")
                    break
                else:
                    print("You failed to flee!")
                    turn_order = "enemy"
        else:
            if attack(enemy, player):
                death()
            turn_order = "player"

    if chest_chance and chest_type and simple_chance(chest_chance):
        open_chest(chest_type)


def open_chest(chest_type):
    """Simulate opening a chest."""
    story_text(f"You found a {rarity_text(chest_type, chest_rarity_dict[chest_type])} chest!")
    items = [item for item, weight in chest_dict[chest_type]]
    weights = [weight for item, weight in chest_dict[chest_type]]
    reward = random.choices(items, weights=weights, k=1)[0]

    if isinstance(reward, int):
        print(f"You found {rarity_text(reward, 'gold')} gold!")
        player.gold += reward
    else:
        print(f"You found a {reward}!")
        add_to_inventory(reward)


def shop_interaction(shop_type):
    """Interact with a shop."""
    shop = shop_dict[shop_type]
    story_text(f"You enter {shop.name}.")
    while True:
        print(f"{rarity_text('GOLD', 'gold')}: {player.gold}")
        for idx, (item, stock) in enumerate(shop.items, start=1):
            print(f"{idx}. {item} - {rarity_text(item.price, 'gold')} (x{stock})")
        choice = choice_text("What do you want to do?", ["Buy", "Sell", "Leave"])
        if choice == 1:
            # Handle buying
            pass
        elif choice == 2:
            # Handle selling
            pass
        elif choice == 3:
            break


def level_1():
    """Define level 1 gameplay."""
    fight(enemy_dict["Goblin"], chest_chance=50, chest_type="Wooden")
    shop_interaction("Village Shop")
    fight(enemy_dict["Fat Goblin"], chest_chance=30, chest_type="Iron")
    story_text("You completed level 1!")


def main():
    """Main game loop."""
    text_boundary('start')
    player.name = input("Enter your character's name: ").strip().capitalize()
    clear()
    level_1()


if __name__ == "__main__":
    main()
