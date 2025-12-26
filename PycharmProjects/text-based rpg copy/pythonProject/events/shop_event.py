from pythonProject.useful_functions.print_functions import clear, story_text, rarity_text, text_boundary, choice_text, view_item, healthbar
from pythonProject.useful_functions.inventory_functions import add_inv, inventory, remove_inv, summon_item, use_inventory, drop_item
from pythonProject.useful_functions.chance_functions import simple_chance

from pythonProject.class_folder.services.shops import shop_dict

from pythonProject.class_folder.equippables.weapons import weapon_dict
from pythonProject.class_folder.equippables.armour import armour_dict

from pythonProject.initial_variables import player, developer, inv


def shop_ui(shop_obj, is_naked=False):
    max_name_length = max(len(shop_object[0].name) for shop_object in shop_obj.items) + 4
    max_price_length = max(len(str(shop_object[0].price)) for shop_object in shop_obj.items) + 5

    print(f'{rarity_text('GOLD', 'gold')}: {player.gold}')
    text_boundary(length=max_name_length + max_price_length + 10)
    print(f"{'':<3}{'Item':<{max_name_length}}{'Price':<{max_price_length}}Amount")

    for idx, item in enumerate(shop_obj.items, start=1):
        formatted_name = f"{item[0].name:<{max_name_length + 2}}"
        print(f"{idx}. {rarity_text(formatted_name, item[0].rarity):<{max_name_length + 2}}"
              f"{str(item[0].price * (2 if is_naked else 1)):<{max_price_length}}{item[1]}")
    text_boundary(length=max_name_length + max_price_length + 10)


def shop(shop_type):
    clear()

    shop_obj = shop_dict.get(shop_type)
    story_text(f"You entered a {shop_obj.name}")

    while True:
        is_naked = False
        if player.armour == armour_dict['Naked']:
            is_naked = True

        shop_ui(shop_obj, is_naked=is_naked)
        option_labels = ["Buy", "Sell", "Inventory"]

        is_rest = False
        if type(shop_obj.rest) is list:
            option_labels.append("Rest")
            is_rest = True
        option_labels.append("Leave")

        if developer['status']:
            option_labels.append(rarity_text('ADD ITEM', 'special'))

        choice = choice_text("What do you do", option_labels)
        clear()

        if choice == 1:
            shop_ui(shop_obj, is_naked=is_naked)

            try:
                print("Which item?")
                item_idx = int(input())

                if not (1 <= item_idx <= len(shop_obj.items)):
                    raise ValueError

                item_tuple = shop_obj.items[item_idx - 1]
                item = item_tuple[0]

                clear()
                shop_ui(shop_obj, is_naked=is_naked)

                if item_tuple[1] == 0:
                    print(f"{str(item)} out of stock")
                    input()
                    clear()
                    continue

                amount = 1
                if item_tuple[1] > 1:
                    print(f"How many {str(item)} do you want?")
                    amount = int(input())

                if not (1 <= amount <= item_tuple[1]):
                    raise ValueError

                if amount == 0:
                    continue

                item_price = item.price * amount * (2 if is_naked else 1)

                if player.gold < item_price:
                    clear()
                    shop_ui(shop_obj, is_naked=is_naked)
                    print(f"You need {rarity_text(str(item_price - player.gold), 'gold')} more gold{', slut' if is_naked else ''}")
                    input()
                    clear()
                    continue

                clear()

                max_name_length = len(item.name) + 4
                max_price_length = len(str(item.price)) + 5
                viewing_item_class = item.__class__.__name__

                print(f'GOLD: {rarity_text(str(player.gold), 'gold')}')

                view_item(item, viewing_item_class, ask_input=False, auto_clear=False)

                choice = choice_text(f"Pay {rarity_text(item_price, 'gold')} "
                                     f"for {str(amount)} {rarity_text(item.name, item.rarity)}?",
                                     ["Yes", "No"])
                if choice == 2:
                    continue
                player.gold -= item_price

                item_class = item.__class__.__name__

                if item_class == 'Potion':
                    add_inv(item, amount)
                    shop_obj.items[item_idx - 1][1] -= amount
                    continue

                while True:
                    clear()
                    inventory('view')
                    choice = choice_text(f"Switch {rarity_text(item.name, item.rarity)}?",
                                         ["Yes", "No", "View"])
                    swapped = False

                    if choice == 1:
                        if item_class == 'Weapon':
                            if player.weapon == weapon_dict['Fists']:
                                del player.weapon
                            else:
                                add_inv(player.weapon)
                            player.weapon = item

                        elif item_class == 'Armour':
                            if player.armour == armour_dict['Naked']:
                                del player.armour
                            else:
                                add_inv(player.armour)
                            player.armour = item

                        swapped = True

                        break

                    elif choice == 2:
                        break

                    elif choice == 3:
                        clear()
                        view_item(player.weapon if item_class == 'Weapon' else player.armour, item_class, current=True)
                        view_item(item, item_class)

                add_inv(item=item, amount=(amount if not swapped else amount - 1))
                shop_obj.items[item_idx - 1][1] -= amount
                clear()

            except ValueError:
                clear()

        elif choice == 2:

            inventory('view')
            choice = choice_text(header='What do you do?', option_labels=['Choose Item', 'Sell All', 'Cancel'])
            clear()

            if choice == 3:
                continue

            if choice == 2:
                inventory('view')

                total_profit = 0
                for item, quantity in list(inv.items()):
                    total_profit += int(round(item.price * 0.7)) * quantity

                confirmation = choice_text(f'Sell all for {rarity_text(str(total_profit), 'gold')} gold?',
                                           ['Yes', 'No'])

                if confirmation == 1:
                    for item, quantity in list(inv.items()):
                        player.gold += int(round(item.price * 0.7)) * quantity
                        remove_inv(item, quantity)

                continue

            clear()

            sell_item_inv_index = inventory('use')
            is_player_obj = False
            if sell_item_inv_index == -1:
                continue

            if sell_item_inv_index.__class__.__name__ in ['Weapon', 'Armour']:
                is_player_obj = True

            if is_player_obj:
                if sell_item_inv_index in [weapon_dict['Fists'], armour_dict['Naked']]:
                    clear()
                    continue

                clear()
                inventory('view')

                choice = choice_text(f"Sell {sell_item_inv_index} for "
                                     f"{rarity_text(text=str(sell_item_inv_index.price), rarity='gold')} gold?",
                                     ["Yes", "No"])
                if choice == 1:
                    player.gold += sell_item_inv_index.price
                    if sell_item_inv_index.__class__.__name__ == 'Weapon':
                        player.weapon = weapon_dict['Fists']

                    if sell_item_inv_index.__class__.__name__ == 'Armour':
                        player.armour = armour_dict['Naked']

                    continue

            sell_item = list(inv.keys())[sell_item_inv_index]

            sell_item_amount = 1

            while inv[sell_item] > 1:
                try:
                    inventory('view')
                    print(f"How many {str(sell_item)} do you want to sell?")
                    sell_item_amount = int(input())
                    clear()

                    if 0 <= sell_item_amount <= inv[sell_item]:
                        break

                except ValueError:
                    clear()
                    continue

            if sell_item_amount == 0:
                continue

            total_price = int(round(sell_item.price * 0.7)) * sell_item_amount

            inventory('view')
            choice = choice_text(f"Sell {sell_item_amount} {str(sell_item)} for "
                                 f"{rarity_text(text=str(total_price), rarity='gold')} gold?",
                                 ["Yes", "No"])

            if choice == 1:
                player.gold += total_price
                remove_inv(sell_item, sell_item_amount)

        elif choice == 3:
            message_list = use_inventory()  # returns a message signifying if item has already been used or is a potion

            if message_list[0] == 'exit':  # item has been dealt with
                continue

            item_key = message_list[1]  # message_list = [message, item_key, item_class]
            item_class = message_list[2]

            if message_list[0] == 'potion':  # item is a potion
                choice = choice_text(f'Use {item_key}', ['Drop', 'View', 'Cancel'])
                if choice == 1:
                    drop_item(item_key)
                elif choice == 2:
                    view_item(item_key, item_class)

        elif choice == 4 and is_rest:
            text_boundary(pos='start')
            healthbar(player)
            text_boundary(pos='end')
            choice = choice_text(f'Rest for {rarity_text(shop_obj.rest[0], 'gold')} gold',
                                 ['Yes', 'No'])
            clear()

            if choice == 1:

                if player.gold < shop_obj.rest[0]:
                    text_boundary(pos='start')
                    healthbar(player)
                    text_boundary(pos='end')
                    print(f'You need {rarity_text(str(shop_obj.rest[0] - player.gold), 'gold')} more gold')
                    input()
                    clear()
                    continue

                player.gold -= shop_obj.rest[0]

                healed = min(shop_obj.rest[1], player.max_health - player.health)
                player.health += healed

                text_boundary(pos='start')
                healthbar(player)
                text_boundary(pos='end')
                print(f'You healed {healed} health')
                input()

            clear()

        elif (choice == len(option_labels) and not developer['status']) or (choice == len(option_labels) - 1 and developer['status']):
            break

        elif choice == len(option_labels) and developer['status']:
            summon_item()

    clear()

    for shop_obj_item in shop_obj.items:
        restock = 0
        while True:
            if simple_chance(40):
                restock += 1
            else:
                break
        shop_obj_item[1] += restock
