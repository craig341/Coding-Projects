import pyperclip

def filter_defi(line):
    split_line = line.split(' ')
    res = ''
    for word in split_line:
        res += word[0]

        if word[0] in ["'", '(']:
            res += word[1]

        if word[-1] in ["'", ')']:
            if word[-2] in punctuation:
                res += word[-2]
            res += word[-1]

        if word[-1] in punctuation:
            res += word[-1]
        res += ' '

    return res[:-1]


punctuation = [',', '.', ';', ':', '?', '!']

with open('definition.txt', 'r') as file:
    defis = file.read()
    split_defis = defis.split('\n')

    for i in range(split_defis.count('')):
        split_defis.remove('')

with open('terms.txt', 'r') as file:
    terms = file.read()
    split_terms = terms.split('\n')

    for i in range(split_terms.count('')):
        split_terms.remove('')

res_dict = {}

for defi in split_defis:
    for j, term in enumerate(split_terms):
        res_dict[term] = filter_defi(split_defis[j])

to_copy = ''

for key in res_dict:
    to_copy += f'{key}8{res_dict[key]}9'
    print(f'{key}8{res_dict[key]}9')

pyperclip.copy(to_copy)


# Make separate .txt files for 'terms' and 'definitions'; add the corresponding text, ensuring they have the same number of lines
