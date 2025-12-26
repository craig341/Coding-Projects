import os
import requests
import json


def clear():
    os.system('clear')


anki_url = "http://localhost:8765"


def send_to_anki(action, params):
    payload = {
        "action": action,
        "version": 6,
        "params": params
    }

    print("Sending request to Anki:", json.dumps(payload, indent=4))

    response = requests.post(anki_url, json=payload)

    response_data = response.json()
    print("Response from Anki:", response_data)

    return response_data


def add_card(deck_name, prev_lines, curr_line, next_lines, title):
    params = {
        "note": {
            "deckName": deck_name,
            "modelName": "Titled Bilingual Lined Text",
            "fields": {
                "Current Line": curr_line,
                "Previous Lines": prev_lines,
                "Next Lines": next_lines,
                "Title": title,
                "Back Extra": ""
            },
            "tags": [],
            "options": {
                "allowDuplicate": False
            }
        }
    }
    result = send_to_anki("addNote", params)
    return result


with open('English', 'r') as file:
    raw_text_eng = file.read()
    eng_lines_text = raw_text_eng.split('\n')

    for i in range(eng_lines_text.count('')):
        eng_lines_text.remove('')

with open('Latin', 'r') as file:
    raw_text_lat = file.read()
    lat_lines_text = raw_text_lat.split('\n')

    for i in range(lat_lines_text.count('')):
        lat_lines_text.remove('')

if len(eng_lines_text) != len(lat_lines_text):
    print("Lines don't match")
    input()

both_lang_tuples = []
for i in range(len(eng_lines_text)):
    both_lang_tuples.append((eng_lines_text[i], lat_lines_text[i]))

prev_lines = []
curr_line = ''
next_lines = both_lang_tuples.copy()
next_lines.pop(0)


def automatic_add():
    deck_name = input('Anki deck name: ')
    title = input('Title of set text: ')
    print()

    prev_lines = []

    for i in range(len(eng_lines_text)):
        curr_line_2 = '{{c1::' + str(both_lang_tuples[i][0]) + '::' + str(both_lang_tuples[i][1]) + '}}'
        prev_lines_2 = '<br>'.join(prev_lines) if prev_lines else ''
        next_lines_2 = '<br>'.join([line[1] for line in next_lines])
        title_2 = title

        add_card(deck_name, prev_lines_2, curr_line_2, next_lines_2, title_2)

        prev_lines.append(both_lang_tuples[i][0])
        if i != len(eng_lines_text) - 1:
            next_lines.pop(0)

    print("All cards have been processed.")


automatic_add()
