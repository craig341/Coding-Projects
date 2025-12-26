from a import distribute_gifts_a
from b import split_budget_b
from c import max_gift_eights_c
from d import max_gifts_of_8_d


def main():
    budget = int(input('budget: '))
    giftees = int(input('giftees: '))

    print(distribute_gifts_a(budget, giftees))
    print(split_budget_b(budget, giftees))
    print(max_gift_eights_c(budget, giftees))
    print(max_gifts_of_8_d(budget, giftees))


if __name__ == '__main__':
    main()
