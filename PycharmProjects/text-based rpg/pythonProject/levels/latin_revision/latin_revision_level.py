from pythonProject.events.fight_event import fight
from pythonProject.useful_functions.print_functions import clear, story_text, choice_text, choice_story_text, gift
from pythonProject.useful_functions.inventory_functions import add_inv

# from pythonProject.levels.latin_revision.latin_revision_objects.latin_revision_items import
# from pythonProject.levels.latin_revision.latin_revision_objects.latin_revision_armour import
from pythonProject.levels.latin_revision.latin_revision_objects.latin_revision_weapon import old_wool_spinner
from pythonProject.levels.latin_revision.latin_revision_objects.latin_revision_enemies import ghost_of_claudia


def latin_revision():
    story_text('You are approached by an old man...')

    choice = choice_story_text(header="'Stranger, my wife died. I am in devastating pain'", option_labels=["'I deliver great sorrow upon this news'", "'ha ha'"])

    if choice == 1:
        gift(old_wool_spinner, 'The old man', 1)

    elif choice == 2:
        fight(ghost_of_claudia)

