import random


class Warrior:
    def __init__(self, health, max_dmg, name):
        self.health = health
        self.max_dmg = max_dmg
        self.name = name

    def attack(self, enemy):
        damage = random.randint(0, self.max_dmg)
        health_after_attack = enemy.health - damage
        enemy.health = health_after_attack if health_after_attack >= 0 else 0
        return damage


def fight(w1, w2, comments=True):
    while w1.health > 0 and w2.health > 0:
        attacker = random.choice((w1, w2))
        defender = w1 if attacker is w2 else w2
        damage = attacker.attack(defender)
        if comments:
            print(f"{attacker.name} attacked. {defender.name} lost {str(damage)} points. "
                  f"{str(defender.health)} points left.")

    winner = w1.name if w2.health is 0 else w2.name
    if comments:
        print(f"{winner} win!!!!")
    return winner


parameters = {
    'health': int(input('Set health: ')),
    'max_dmg': int(input('Set max damage: '))
}

name_first_warrior = input('Set name for the first warrior: ')
name_second_warrior = input('Set name for the second warrior: ')

warrior_1 = Warrior(**parameters, name=name_first_warrior)
warrior_2 = Warrior(**parameters, name=name_second_warrior)

fight(warrior_1, warrior_2)
