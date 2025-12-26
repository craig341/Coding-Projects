from pythonProject.useful_functions.print_functions import clear, story_text, choice_text, rarity_text
from pythonProject.useful_functions.inventory_functions import inventory, remove_inv

from pythonProject.initial_variables import inv, player

from pythonProject.class_folder.services.merchants import merchant_dict


def merchant(merchant_type):
    clear()

    merchant_obj = merchant_dict.get(merchant_type)
    story_text(f"You encounter a wandering {merchant_obj.name}")

    while True:
        if not inv:
            story_text('You have nothing to sell')
            return

        inventory('view')
        choice = choice_text('Do you want to sell?', ['Yes', 'No'])
        clear()

        if choice == 1:
            sell_item_inv_index = inventory('use')

            if sell_item_inv_index == -1:
                continue
            if sell_item_inv_index == player.weapon or sell_item_inv_index == player.armour:
                print()
                print('Unable to sell')
                input()
                clear()
                continue
            else:
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

            sell_item_class = sell_item.__class__.__name__
            if sell_item_class not in ['Armour', 'Weapon']:
                # if sell_item.item_type != 'potion':
                if sell_item_class != 'Potion':
                    print('moo')
                    sell_item_class = str(sell_item.item_type).capitalize()


            # total_price = int(round(sell_item.price * merchant_obj.bias[sell_item_class])) * sell_item_amount
            total_price = int(round(sell_item.price * merchant_obj.bias[sell_item_class])) * sell_item_amount

            inventory('view')
            choice = choice_text(f"Sell {sell_item_amount} {str(sell_item)} for "
                                 f"{rarity_text(text=str(total_price), rarity='gold')} gold?",
                                 ["Yes", "No"])

            if choice == 1:
                player.gold += total_price
                remove_inv(sell_item, sell_item_amount)

        elif choice == 2:
            return
