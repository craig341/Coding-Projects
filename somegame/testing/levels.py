# # Display all ANSI color codes
# for code in range(256):
#     print(f'\033[38;5;{code}mColour \033[38;5;{code}m\\033[38;5;{code}m\033[0m')

char = "'"

print('\n'.join([f'\033[38;5;{code}mColour {char}\033[38;5;{code}m\\033[38;5;{code}m{char}\033[0m' for code in range(256)]))
print('\n' * 2)

normal = '\033[0m'

code1 = '\033[38;5;3m'
print(code1 + 'hey babes' + normal)

code2 = '\033[38;5;246m'
print(code2 + 'hey babes' + normal)

code3 = '\033[38;5;173m'

print(code3 + 'hey babes' + normal)

print('normal')
