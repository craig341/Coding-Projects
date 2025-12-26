import pyperclip

punctuation = {',', '.', ';', ':', '?', '!', '-'}


def filter_text(text):
    result = []
    word_started = False

    for char in text:
        if char.isalnum():
            if not word_started:
                if result:
                    result.append(' ')
                result.append(char)
                word_started = True
        elif char in punctuation or char.isspace():
            word_started = False
            result.append(char)

    return ''.join(result)


def string_to_dicts(input_string):
    return [
        {line.split('\t')[0]: line.split('\t')[1]}
        for line in input_string.split('\n') if '\t' in line
    ]


with open('input.txt', 'r') as file:
    raw = file.read()

output_dicts = string_to_dicts(raw)

for my_dict in output_dicts:
    for k in my_dict:
        my_dict[k] = filter_text(my_dict[k])

res = []

for my_dict in output_dicts:
    for k, v in my_dict.items():
        res.append(f"{k}\t{v}")
    res.append('\n')

result_string = ''.join(res)
pyperclip.copy(result_string)