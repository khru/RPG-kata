class Character:
    health = 1000
    level = 1
    isAlive = True

    def attack(self, defending_character):
        defending_character.health -= 10
