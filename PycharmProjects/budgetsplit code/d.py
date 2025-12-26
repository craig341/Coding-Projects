def prompt():
    # gemini prompt

    pass


def max_gifts_of_8_d(num_giftees, budget):
    max_gifts_8 = budget // 8

    for gifts_8 in range(max_gifts_8, -1, -1):
        remaining_budget = budget - (gifts_8 * 8)
        remaining_giftees = num_giftees - gifts_8

        if remaining_giftees == 0:
            if remaining_budget == 0:
                return gifts_8
            else:
                continue

        if remaining_budget % remaining_giftees == 0 and remaining_budget // remaining_giftees != 4:
            return gifts_8

        if remaining_giftees * 8 <= remaining_budget:
            continue
    return 0


