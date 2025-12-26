from pythonProject.classes import Entity
# from pythonProject.levels.latin_revision.latin_revision_objects.latin_revision_items import
from pythonProject.levels.latin_revision.latin_revision_objects.latin_revision_armour import toga
from pythonProject.levels.latin_revision.latin_revision_objects.latin_revision_relics import not_so_beautiful_tomb
from pythonProject.levels.latin_revision.latin_revision_objects.latin_revision_weapon import phantom_wool_spinner

from pythonProject.class_folder.equippables.relics import none


ghost_of_claudia = Entity(
    name="Ghost Of Claudia",
    strength=0,
    health=7,
    speed=3,
    aim=50,
    crit_chance=-10,
    crit_multiplier=1,
    max_health=7,
    weapon=phantom_wool_spinner,
    armour=toga,
    relic=none,
    drop_pool={phantom_wool_spinner: 50, not_so_beautiful_tomb: 100},
    gold=12
)

# ghost_of_claudia.view_enemy()
#
# print()
# print()
# from pythonProject.initial_variables import player
#
# player.view_enemy(ask_input=True)