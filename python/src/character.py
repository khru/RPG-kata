class Character:
    health = 1000
    level = 1
    isAlive = True

    def attack(self, defending_character, damage = 10):
        defending_character.health -= damage
        if defending_character.health <= 0:
            defending_character.health = 0
            defending_character.isAlive = False

    def heal(self, defending_character, heal):
        defending_character.health += heal


