def prompt():
    print('(Made recently)')
    print("""
    
Write python code to split a given budget (money) based on the number of (giftees)

Gifts must not contain the amount 4
You want to give the amount 8

The code should return number of gifts equal to 8 following the rules:
Spend the entire budget 
Do not give 4s
Do not give 0s unless it is physically impossible not to (for example splitting 1 money for 2 people)
Return the maximum of 8s given to a number of giftees following the constraints

""")


def max_gift_eights_c(budget, giftees):
    if budget < giftees:
        return -1

    if budget <= 4 and budget % 4 == 0:
        return -1

    if budget == 8 and giftees == 1:
        return 1

    max_eights = budget // 8

    remaining_budget = budget % 8

    if remaining_budget == 4:
        max_eights -= 1
        remaining_budget += 8

    if remaining_budget > giftees:
        return max_eights

    return max_eights
