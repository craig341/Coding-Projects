def prompt():
    print("""
    
Write python code to split a given budget (money) based on the number of (giftees)
    
Gifts must not contain the amount 4
You want to give the amount 8

The code should return number of gifts equal to 8 following the rules:
Spend the entire budget 
Do not give 4s
Do not give 0s unless not enough money
Give the maximum of 8s given a number of giftees

""")


def distribute_gifts_a(budget, giftees):
    max_eights = budget // 8
    remaining_budget = budget % 8

    while max_eights > giftees or (remaining_budget != 0 and max_eights + 1 < giftees):
        max_eights -= 1
        remaining_budget += 8

    if max_eights == giftees:
        remainder = remaining_budget
    else:
        remainder = budget - max_eights * 8

    gifts = [8] * max_eights
    if max_eights < giftees:
        other_gifts = [remainder] + [0] * (giftees - max_eights - 1)
        gifts.extend(other_gifts)

    for i in range(len(gifts)):
        if gifts[i] == 4:
            gifts[i] = 2 + 2
        elif gifts[i] == 0:
            gifts[i] = 0

    if 0 in gifts and budget >= giftees:
        gifts = [1 if gift == 0 else gift - 1 for gift in gifts]

    if sum(gifts) != budget:
        return "Budget can't be split as required."

    return gifts
