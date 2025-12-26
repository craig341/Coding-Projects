import pyperclip
import re

with open('text.txt', 'r') as file:
    raw_text = file.read()
    text_list = raw_text.split('\n')

    for i in range(text_list.count('')):
        text_list.remove('')

res = []

for line in text_list:
    pattern = r"([,.;:?!'\(\)\{\}-])|\s+"

    split_text = re.split(pattern, line)

    for _ in range(split_text.count('')):
        split_text.remove('')

    for i, v in enumerate(split_text):
        if v is None:
            split_text[i] = ' '

    for i, v in enumerate(split_text):
        if v.isalpha():
            split_text[i] = v[0]

    filtered_line = ''.join(split_text)
    res.append(filtered_line)

to_copy = ''

for line in res:
    to_copy += line
    to_copy += '\n'

to_copy = to_copy[0:-1]

print(to_copy)
pyperclip.copy(to_copy)
