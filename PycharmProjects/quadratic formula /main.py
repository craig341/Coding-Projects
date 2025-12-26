import math


def format_number(num):
    return int(num) if num.is_integer() else num


skip = False
print('In the form ax² + bx + c')
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
print()

print(f'{format_number(a)}x² + {format_number(b)}x + {format_number(c)} = 0')

print()

top_length_1 = 20 + (2 * (len(str(format_number(b)))) + len(str(format_number(a))) + len(str(format_number(c))))
bottom_length_1 = 4 + len(str(format_number(a)))
bottom_gap_length_1 = (top_length_1 - bottom_length_1) // 2

top_length_2 = 9 + ((len(str(format_number(b)))) + len(str(format_number(b ** 2))) + len(str(format_number(4 * a * c))))
bottom_length_2 = len(str(format_number(2 * a)))
bottom_gap_length_2 = (top_length_2 - bottom_length_2) // 2

top_length_3 = 6 + ((len(str(format_number(b)))) + len(str(format_number(b ** 2 - 4 * a * c))))
bottom_gap_length_3 = (top_length_3 - bottom_length_2) // 2

print(f'x = -({format_number(b)}) ± ⎷({format_number(b)}² - 4 * {format_number(a)} * {format_number(c)})')
print(4 * ' ' + top_length_1 * '‾')
print(4 * ' ' + bottom_gap_length_1 * ' ' + f'2 * {format_number(a)}' + bottom_gap_length_1 * ' ')

if input().lower() == 'skip':
    skip = True
print()

print(f'x = {format_number(b * -1)} ± ⎷({format_number(b ** 2)} - {format_number(4 * a * c)})')
print(4 * ' ' + top_length_2 * '‾')
print(4 * ' ' + bottom_gap_length_2 * ' ' + f'{format_number(2 * a)}' + bottom_gap_length_2 * ' ')

if not skip:
    input()
print()

print(f'x = {format_number(b * -1)} ± ⎷({format_number(b ** 2 - 4 * a * c)})')
if 2 * a != 1:
    print(4 * ' ' + top_length_3 * '‾')
    print(4 * ' ' + bottom_gap_length_3 * ' ' + f'{format_number(2 * a)}' + bottom_gap_length_3 * ' ')

if not skip:
    input()
print('===============================')
print()

discriminant = b ** 2 - 4 * a * c
if discriminant < 0:
    print('No real solutions')
else:
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (b * -1 + sqrt_discriminant) / (2 * a)
    x2 = (b * -1 - sqrt_discriminant) / (2 * a)

    print(f'x = {format_number(b * -1)} + ⎷({format_number(discriminant)}) = {format_number(x1)}')
    if 2 * a != 1:
        print(4 * ' ' + top_length_3 * '‾')
        print(4 * ' ' + bottom_gap_length_3 * ' ' + f'{format_number(a)}' + bottom_gap_length_3 * ' ')
    print()
    print(f'x = {format_number(b * -1)} - ⎷({format_number(discriminant)}) = {format_number(x2)}')
    if 2 * a != 1:
        print(4 * ' ' + top_length_3 * '‾')
        print(4 * ' ' + bottom_gap_length_3 * ' ' + f'{format_number(a)}' + bottom_gap_length_3 * ' ')
