import os
from entity import Entity


player = Entity(name='dave')
enemy = Entity(name='enemy', health=50, strength=5, speed=2)

while True:
    print('\n'*80)

    player.attack(enemy)
    enemy.attack(player)

    player.health_bar.draw()
    enemy.health_bar.draw()

    input()