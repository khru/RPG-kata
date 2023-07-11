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
