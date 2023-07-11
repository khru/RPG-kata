class Character:
    health = 1000
    level = 1
    isAlive = True

    def attack(self, defending_character, damage = 10):
        defending_character.health -= damage
