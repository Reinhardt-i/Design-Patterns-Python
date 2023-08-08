from typing import List


class TextEditor:
    def __init__(self, content: str):
        self._content = content

    def get_content(self) -> str:
        return self._content

    def set_content(self, content: str) -> None:
        self._content = content

    def create_memento(self) -> 'Memento':
        return Memento(self._content)

    def restore_from_memento(self, memento: 'Memento') -> None:
        self._content = memento.get_content()


class Memento:
    def __init__(self, content: str):
        self._content = content

    def get_content(self) -> str:
        return self._content


# Caretaker AKA HISTORY!
class Caretaker:
    def __init__(self):
        self._mementos: List['Memento'] = []

    def add_memento(self, memento: 'Memento') -> None:
        self._mementos.append(memento)

    def get_memento(self, index: int) -> 'Memento':
        return self._mementos[index]


if __name__ == '__main__':
    text_editor = TextEditor("Hello, World!")
    caretaker = Caretaker()

    # Save the initial state
    caretaker.add_memento(text_editor.create_memento())

    # Make some changes
    text_editor.set_content("Hello, OpenAI!")
    # Save the new state
    caretaker.add_memento(text_editor.create_memento())

    # Make more changes
    text_editor.set_content("Hello, GPT-3!")

    # Restore the first state
    text_editor.restore_from_memento(caretaker.get_memento(0))
    print(text_editor.get_content())  # Output: Hello, World!

    # Restore the second state
    text_editor.restore_from_memento(caretaker.get_memento(1))
    print(text_editor.get_content())  # Output: Hello, OpenAI!
    