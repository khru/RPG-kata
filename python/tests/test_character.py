from src.character import Character


class TestChangeMe:

    def test_character_creation(
            self,
    ):
        # Given
        character = Character()
        # When

        # Then
        assert character.health == 1000
        assert character.level == 1
        assert character.isAlive == True

    def test_character_can_deal_damage_to_other_character(
            self,
    ):
        # Given
        defending_character = Character()
        attacking_character = Character()
        # When
        attacking_character.attack(defending_character)
        # Then
        assert defending_character.health == 990

    def test_character_can_attack_twice_to_other_character(
            self,
    ):
        # Given
        defending_character = Character()
        attacking_character = Character()
        # When
        attacking_character.attack(defending_character)
        attacking_character.attack(defending_character)
        # Then
        assert defending_character.health == 980

    def test_character_can_attack_with_specific_damage(
            self,
    ):
        # Given
        defending_character = Character()
        attacking_character = Character()
        # When
        attacking_character.attack(defending_character, 200)
        # Then
        assert defending_character.health == 800

    def test_character_can_kill_other_character(
            self,
    ):
        # Given
        defending_character = Character()
        attacking_character = Character()

        # When
        attacking_character.attack(defending_character, 1000)

        # Then
        assert defending_character.health == 0
        assert defending_character.isAlive == False

    def test_character_can_not_have_negative_health(self):
        # Given
        defending_character = Character()
        attacking_character = Character()

        # When
        attacking_character.attack(defending_character, 3000)

        # Then
        assert defending_character.health == 0
        assert defending_character.isAlive == False

