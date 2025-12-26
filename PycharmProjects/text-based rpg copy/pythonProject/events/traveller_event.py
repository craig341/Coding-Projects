from pythonProject.useful_functions.print_functions import clear, story_text, choice_text


def traveller():
    clear()
    story_text('You encounter a mysterious traveller')

    choice_text('Do you want to make a deal', ['Yes', 'No'])

    class PrizePool:
        def __init__(self, price, weapons, potions, armour):
            self.price = price
            self.weapons = weapons
            self.potions = potions
            self.armour = armour

    small_prize = PrizePool(price=20,
                            weapons=[
                                'Cane',
                                'Bendy Wand', 'Wooden Sword', 'Leaf Blade',
                            ],
                            potions=[

                            ],
                            armour=[

                            ])
