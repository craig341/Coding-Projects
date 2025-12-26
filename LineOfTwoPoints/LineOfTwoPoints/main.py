from math import sqrt


title_barrier = '=========================='

def point_input():
    p1_raw = input("Point 1: ")
    p2_raw = input("Point 2: ")
    print(title_barrier)

    p1 = point_cleanup(p1_raw)
    p2 = point_cleanup(p2_raw)

    return p1, p2


def point_cleanup(point_raw):
    point_list = list(point_raw.strip())

    for i, char in enumerate(point_list):
        if not char.isnumeric() and char not in ['-', ',', '/', '.']:
            point_list.remove(point_list[i])

    x_value = ''
    y_value = ''
    found_comma = False
    for char in point_list:
        if char == ',':
            found_comma = True
            continue

        if not found_comma:
            x_value += char

        if found_comma:
            y_value += char



    def fraction_to_decimal(value):
        numerator = ''
        denominator = ''
        found_slash = False
        for char in value:
            if char == '/':
                found_slash = True
                continue

            if not found_slash:
                numerator += char

            if found_slash:
                denominator += char

        decimal_value = float(numerator) / float(denominator)
        return str(decimal_value)

    if '/' in x_value:
        x_value = fraction_to_decimal(x_value)

    if '/' in y_value:
        y_value = fraction_to_decimal(y_value)

    point = (float(x_value), float(y_value))

    return point


def calculate_choice(p1, p2):
    print("""Calculate:
    1. Length
    2. Midpoint
    3. Gradient
    4. All
    5. Choose new points""")
    choice = int(input())
    print(title_barrier)

    if choice == 1:
        length(p1, p2)
        print(title_barrier)

    if choice == 2:
        midpoint(p1, p2)
        print(title_barrier)

    if choice == 3:
        gradient(p1, p2)
        print(title_barrier)

    if choice == 4:
        print('Length:')
        length(p1, p2)
        print()

        print('Midpoint:')
        midpoint(p1, p2)
        print()

        print('Gradient:')
        gradient(p1, p2)

        print(title_barrier)

    if choice == 5:
        print()
        print()
        print(title_barrier)
        main()

    else:
        calculate_choice(p1, p2)


def length(p1, p2):
    print(f'length² = ({p1[0]:}-{p2[0]:})² + ({p1[1]}-{p2[1]})²')
    print(f'length² = ({p1[0] - p2[0]})² + ({p1[1] - p2[1]})²')
    print(f'length² = {(p1[0] - p2[0]) ** 2} + {(p1[1] - p2[1]) ** 2}')
    print(f'length² = {((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)}')
    print(f'length = ⎷{((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)}')
    print(f'length = {sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))}')



def midpoint(p1, p2):
    print(f'mid = ( [{p1[0]} + {p2[0]}]/2 , [{p1[1]} + {p2[1]}]/2 )')
    print(f'mid = ( [{p1[0] + p2[0]}]/2 , [{p1[1] + p2[1]}]/2 )')
    print(f'mid = ({(p1[0] + p2[0])/2}, {(p1[1] + p2[1])/2})')


def gradient(p1, p2):
    print(f'm = ( [{p1[1]} - {p2[1]}] / [{p1[0]} - {p2[0]}] )')
    print(f'm = ( {p1[1] - p2[1]} / {p1[0] - p2[0]} )')
    print(f'm = {(p1[1] - p2[1]) / (p1[0] - p2[0])}')


def main():
    p1, p2 = point_input()
    calculate_choice(p1, p2)


if __name__ == '__main__':
    main()
