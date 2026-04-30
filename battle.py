import random

player = {
    "name": "Pikachu",
    "hp": 35,
    "attack": 12
}

enemy = {
    "name": "Charmander",
    "hp": 39,
    "attack": 10
}

def use_potion(character):
    character["hp"] += 10
    print(f'{character["name"]} used a potion and recovered 10 HP!')

def attack(attacker, defender):
    damage = random.randint(5, attacker["attack"])

    if random.random() < 0.25:
        damage *= 2
        print("Critical hit!")

    defender["hp"] -= damage
    print(f'{attacker["name"]} attacks {defender["name"]} for {damage} damage!')


def show_status():
    print(f'{player["name"]}: {player["hp"]} HP')
    print(f'{enemy["name"]}: {enemy["hp"]} HP')


print("A wild Charmander appears!")
show_status()

attack(player, enemy)
attack(enemy, player)

use_potion(player)

print("\nAfter one round:")
show_status()