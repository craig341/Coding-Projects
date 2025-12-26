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


def split_budget_b(budget, giftees):
    max_gifts_of_8 = budget // 8

    num_gifts_of_8 = min(max_gifts_of_8, giftees)

    remaining_budget = budget - (num_gifts_of_8 * 8)

    if remaining_budget == 0 and num_gifts_of_8 == giftees:
        return [8] * num_gifts_of_8

    if num_gifts_of_8 < giftees:
        remaining_giftees = giftees - num_gifts_of_8

        if remaining_budget == 0:
            return [8] * num_gifts_of_8 + [1] * remaining_giftees

        if remaining_budget <= remaining_giftees:
            return [8] * num_gifts_of_8 + [1] * (remaining_budget) + [0] * (remaining_giftees - remaining_budget)

    return []
