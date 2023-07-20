from typing import Dict


class Character:
    """
    Character interface that defines the display method for characters.
    """

    def display(self, weapon: str) -> None:
        """
        Displays the character with the specified weapon.
        """
        pass


class CharacterImpl(Character):
    """
    Concrete implementation of the Character interface.
    """

    def __init__(self, character_type: str):
        self.character_type = character_type

    def display(self, weapon: str) -> None:
        print(f"Character type: {self.character_type}, Weapon: {weapon}")


class CharacterFactory:
    """
    Flyweight factory that creates and caches character objects.
    """

    character_cache: Dict[str, Character] = {}

    @staticmethod
    def get_character(character_type: str) -> Character:
        """
        Returns a character object from the cache, or creates a new one if not present.
        """
        character = CharacterFactory.character_cache.get(character_type)

        if character is None:
            character = CharacterImpl(character_type)
            CharacterFactory.character_cache[character_type] = character

        return character


if __name__ == '__main__':
    character1 = CharacterFactory.get_character("Warrior")
    character1.display("Sword")

    character2 = CharacterFactory.get_character("Mage")
    character2.display("Staff")

    character3 = CharacterFactory.get_character("Warrior")
    character3.display("Axe")
    