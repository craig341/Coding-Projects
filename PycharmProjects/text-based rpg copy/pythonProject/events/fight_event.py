from pythonProject.useful_functions.print_functions import story_text, clear, text_boundary, healthbar, rarity_text, \
    death, choice_text, view_item
from pythonProject.useful_functions.chance_functions import simple_chance, randomise_variable
from pythonProject.useful_functions.inventory_functions import add_inv, inventory, remove_inv, summon_item, drop_item, \
    use_inventory

from pythonProject.class_folder.equippables.weapons import weapon_dict
from pythonProject.class_folder.equippables.armour import armour_dict

from pythonProject.class_folder.services.chests import chest_dict
from pythonProject.class_folder.services.shops import shop_dict
from pythonProject.class_folder.services.merchants import merchant_dict

from pythonProject.class_folder.entities import enemy_dict

from pythonProject.events.chest_event import chest
from pythonProject.events.shop_event import shop
from pythonProject.events.merchant_event import merchant

from pythonProject.initial_variables import player, inv

import pythonProject.initial_variables

import random


def fight_ui(enemy, turn):
    text_boundary(middle=f'Turn {turn}')
    healthbar(player)
    print()
    healthbar(enemy, player=False)
    text_boundary()


def fight(enemy, chest_chance=0, chest_type=None, entrance_text='You encounter'):
    input(pythonProject.initial_variables.developer)
    story_text(f'{entrance_text} {enemy.name}')
    clear()

    def attack(attacker=player, victim=enemy, developer_prediction=False):
        attacker_strength, attacker_aim = player_fight_strength, player_fight_aim  # temporary battle stats
        if attacker == enemy:
            attacker_strength, attacker_aim = enemy_fight_strength, enemy_fight_aim

        if attacker.weapon.durability != -1 and random.randint(1,
                                                               attacker.weapon.durability) == 1:  # determine if weapon breaks
            attacker.weapon = weapon_dict['Fists']

            fight_ui(enemy, turn)
            print(f'{'Your' if attacker == player else enemy.name} weapon broke')
            input()
            clear()
            return

        if not simple_chance(
                min(attacker_aim + attacker.weapon.aim, 99)) and not developer_prediction:  # determine if attack missed
            fight_ui(enemy, turn)
            print(f'{'You' if attacker == player else enemy.name} missed')
            input()
            clear()
            return

        total_damage = attacker_strength + attacker.weapon.damage

        if not developer_prediction:  # unrandomised total_dmg for developer base dmg prediction
            randomise_variable(total_damage)  # total_dmg randomised between 50% boundaries

        is_crit = False
        crit_chance = int(round((
                                            attacker.crit_chance + attacker.weapon.crit_chance + attacker.armour.crit_chance) * attacker_aim / 100))  # calcylate int crit chance
        crit_multiplier = int(
            round((attacker.crit_multiplier + attacker.weapon.crit_multiplier + attacker.armour.crit_multiplier) / 3))

        if developer_prediction:
            return total_damage, attacker_aim, crit_chance  # return developer predictions before variables randomised

        if simple_chance(crit_chance if crit_chance > 0 else 1):  # crit chance always >= 1
            is_crit = True
            total_damage *= crit_multiplier  # crit chance doubles dmg

        if simple_chance(90):  # 10% ignore armour defence
            total_damage -= victim.armour.defense
            total_damage = max(total_damage, 0)  # dmg always >= 0

        victim.health -= total_damage
        fight_ui(enemy, turn)

        print(f'{'You' if attacker == player else enemy.name} dealt '
              f'{rarity_text(total_damage, 'crit' if is_crit else 'default')} damage')

        if victim.health <= 0:  # detects if victim was killed
            if attacker == player:  # if victim was enemy
                gold_drop = randomise_variable(enemy.gold)  # drop enemy gold
                print(f'{enemy.name} is dead, +{rarity_text(gold_drop, 'gold')}')
                player.gold += gold_drop

                for item, drop_chance in enemy.drop_pool.items():
                    if simple_chance(drop_chance):
                        print(f'{enemy.name} dropped {item}')
                        add_inv(item)
                input()

                return 'player win'  # returns player wins

            if attacker == enemy:  # if victim was player
                input()
                death()  # death screen

        input()
        clear()

    flee = False
    turn = 1
    potion_cooldown = {}
    developer_event_list = []

    player_fight_strength = player.strength
    player_fight_speed = player.speed
    player_fight_aim = player.aim

    enemy_fight_strength = enemy.strength
    enemy_fight_speed = enemy.speed
    enemy_fight_aim = enemy.aim
    og_enemy_weapon = enemy.weapon
    og_enemy_armour = enemy.armour

    while True:
        keys_to_remove = [key for key in potion_cooldown if
                          potion_cooldown[key] == turn]  # list of potions that have run out

        for key in keys_to_remove:  # restore stats after potion runs out
            player_fight_strength -= key.attribute_changes[0]
            player_fight_speed -= key.attribute_changes[2]
            player_fight_aim -= key.attribute_changes[3]
            del potion_cooldown[key]

        player_fight_speed += player.weapon.speed + player.armour.speed  # calculate total player speed
        enemy_fight_speed += enemy.weapon.speed + enemy.armour.speed  # calculate total enemy speed

        first_attacker = player  # set player as first attacker
        second_attacker = enemy

        if player_fight_speed < enemy_fight_speed:  # set enemy as first attacker if faster
            first_attacker = enemy
            second_attacker = player

        elif player_fight_speed == enemy_fight_speed:  # 50/50 for first attacker, if same speed
            if simple_chance(50):
                first_attacker = enemy
                second_attacker = player

        player_fight_speed -= player.weapon.speed + player.armour.speed  # player base speed instead of total speed
        enemy_fight_speed -= enemy.weapon.speed + enemy.armour.speed  # enemy base speed instead of total speed

        fight_ui(enemy, turn)
        option_labels = ['Attack', 'Item', 'Run']
        if pythonProject.initial_variables.developer:  # adding developer options
            option_labels.append(rarity_text('PREDICT THE FUTURE', 'special'))
            option_labels.append(rarity_text('STATS', 'special'))
            option_labels.append(rarity_text('ADD EVENT', 'special'))
            option_labels.append(rarity_text('ADD ITEM', 'special'))

        choice = choice_text('What do you do', option_labels)
        clear()

        if choice == 1:  # Attack
            if attack(attacker=first_attacker, victim=second_attacker) == 'player win':  # first attacker
                break  # if player won, fight loop broken

            if attack(attacker=second_attacker, victim=first_attacker) == 'player win':  # second attacker
                break  # if player won, fight loop broken
            turn += 1  # turn increases after both fighters attacked

        elif choice == 2:  # Item
            message_list = use_inventory()  # returns a message signifying if item has already been used or is a potion

            if message_list[0] == 'exit':  # item has been dealt with
                continue

            item_key = message_list[1]  # message_list = [message, item_key, item_class]
            item_class = message_list[2]

            if message_list[0] == 'potion':  # item is a potion
                choice = choice_text(f'Use {item_key}', ['Use', 'Drop', 'View', 'Cancel'])
                clear()
                if choice == 1:
                    if item_key in potion_cooldown:  # potions on cooldown in dictionary
                        inventory('view')
                        print(
                            f'{item_key} on cooldown for {potion_cooldown[item_key] - turn} '  # turns left on cooldown 
                            f'{'turn' if potion_cooldown[item_key] - turn == 1 else 'turns'}')  # single/plural
                        input()
                        clear()
                    else:
                        player.health += min(item_key.attribute_changes[1],
                                             player.max_health - player.health)  # health changes, cannot heal over max health
                        if player.health <= 0:  # health changes can never kill player
                            player.health = 1

                        player_fight_strength += item_key.attribute_changes[0]  # strength changes
                        player_fight_speed += item_key.attribute_changes[2]  # speed changes
                        player_fight_aim += item_key.attribute_changes[3]  # aim changes

                        if item_key.duration > 0:  # adding potion to cooldown dict, if there is duration
                            potion_cooldown[item_key] = turn + item_key.duration  # {potion: turn cooldown ends}

                        remove_inv(item_key)  # potion used, removed

                elif choice == 2:
                    drop_item(item_key)

                elif choice == 3:
                    view_item(item_key, item_class)

        elif choice == 3:  # run

            if player_fight_speed == enemy_fight_speed:  # if speeds are same, 50/50 to flee
                flee_chance = 50

            elif player_fight_speed + enemy_fight_speed <= 0:  # one speed is negatively same or larger
                if player_fight_speed > enemy_fight_speed:
                    flee_chance = 95  # if player faster, flee chance maxed
                else:
                    flee_chance = 5  # if enemy faster, flee chance minimised
            else:
                flee_chance = max(5, min(95, int(round(
                    (player_fight_speed / (player_fight_speed + enemy_fight_speed)))) * 100))  # flee chance 5-95

            if first_attacker == enemy:  # enemy attacks before flee, if enemy is first attacker
                attack(attacker=first_attacker, victim=second_attacker)

            fight_ui(enemy, turn)
            if simple_chance(flee_chance):  # determines successful flee
                flee = True
                print('You ran away')
                input()
                clear()
                break
            else:
                print("You couldn't run away")
                input()
                clear()

            if first_attacker == player:  # enemy attacks after flee, if enemy is second attacker
                attack(attacker=enemy, victim=player)

        elif choice == 4 and pythonProject.initial_variables.developer:  # PREDICT THE FUTURE
            first_attacker_name = rarity_text('PLAYER', 'uncommon')  # player written in uncommon colour, like healthbar
            second_attacker_name = rarity_text(enemy.name, 'bleed')  # enemy written in bleed colour, like healthbar
            if first_attacker == enemy:
                first_attacker_name = rarity_text(enemy.name, 'bleed')
                second_attacker_name = rarity_text('PLAYER', 'uncommon')

            first_total_dmg, first_aim, first_crit = attack(attacker=first_attacker, victim=second_attacker,
                                                            developer_prediction=True)
            first_total_dmg -= second_attacker.armour.defense

            print(f'{first_attacker_name} attacks first')

            print(f'Deals {first_total_dmg} base damage '
                  f'{rarity_text('KO', 'bleed') if first_total_dmg >= second_attacker.health else ''}')

            print(f'{first_aim}% hit chance')
            print(f'{first_crit if first_crit > 0 else 1}% {rarity_text('crit', 'crit')}')
            print('10% ignore armour')
            print()

            second_total_dmg, second_aim, second_crit = attack(attacker=second_attacker, victim=first_attacker,
                                                               developer_prediction=True)
            second_total_dmg -= first_attacker.armour.defense

            print(f'{second_attacker_name} attacks second')

            print(f'Deals {second_total_dmg} base damage '
                  f'{rarity_text('KO', 'bleed') if second_total_dmg >= first_attacker.health else ''}')

            print(f'{second_aim}% hit chance')
            print(f'{second_crit if second_crit > 0 else 1}% {rarity_text('crit', 'crit')}')
            print('10% ignore armour')
            print()
            input()

        elif choice == 5 and pythonProject.initial_variables.developer:
            from pythonProject.class_folder.entities import display_entity

            display_entity(player)
            print()
            display_entity(enemy)

            input()

        elif choice == 6 and pythonProject.initial_variables.developer:
            if developer_event_list:
                print(developer_event_list)
            choice = choice_text('Which event type', ['CHEST', 'SHOP', 'MERCHANT', 'ENEMY', 'CANCEL'])

            if choice == 5:
                continue

            event = 'chest'
            event_dict = chest_dict
            if choice == 2:
                event = 'shop'
                event_dict = shop_dict
            elif choice == 3:
                event = 'merchant'
                event_dict = merchant_dict
            elif choice == 4:
                event = 'enemy'
                event_dict = enemy_dict

            clear()
            choice = choice_text('Options', ['ADD', 'MULTIADD', 'LIST'])

            if choice == 1 or choice == 2:
                print(f'Enter {event} type: ')
                event_input = input().title()
                print()

                if event_input in event_dict:
                    event_amount = 1

                    if choice == 2:
                        try:
                            print('How many events')
                            event_amount = int(input())
                            print()

                        except ValueError:
                            print('Invalid number')
                            print()

                        for _ in range(event_amount):
                            developer_event_list.append([event_input, event])

                    print(f'{event_amount} ', end='')

                    if event_dict == chest_dict:
                        print(
                            f"'{rarity_text(event_input, event_dict[event_input].rarity)}' chest{'s' if event_amount > 1 else ''} added to event queue")
                    else:
                        print(f"'{event_input}' added to event queue")
                    developer_event_list.append([event_input, event])
                    input()
                    clear()

                else:
                    print(
                        f"'{event_input}' not in {'chest_dict' if event_dict == chest_dict else 'shop_dict' if event_dict == shop_dict else 'merchant_dict' if event_dict == merchant_dict else 'enemy_dict'}")
                    input()
                    clear()

            elif choice == 3:
                for i in event_dict:
                    print(i)
                input()
                clear()

        elif choice == 7 and pythonProject.initial_variables.developer:
            summon_item()

    enemy.health = enemy.max_health
    enemy.weapon = og_enemy_weapon  # if weapon broken, weapon fixed
    enemy.armour = og_enemy_armour  # if armour broken, armour fixed

    if simple_chance(chest_chance) and not flee and chest_type:  # no chest if player fleed
        chest(chest_type)
    else:
        clear()

    if developer_event_list:
        for event, event_type in developer_event_list:
            if event_type == 'chest':
                chest(event)
            elif event_type == 'shop':
                shop(event)
            elif event_type == 'merchant':
                merchant(event)
            elif event_type == 'enemy':
                fight(enemy_dict[event])
