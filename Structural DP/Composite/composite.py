from abc import ABC, abstractmethod
from typing import List


# FileSystemComponent interface
class FileSystemComponent(ABC):
    @abstractmethod
    def display_details(self) -> None:
        """
        Display details of the file system component.
        """
        pass


# File class implementing FileSystemComponent -Leaf!
class File(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name

    def display_details(self) -> None:
        """
        Display details of the file.
        """
        print(f"File: {self.name}")


# Directory class implementing FileSystemComponent
class Directory(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List[FileSystemComponent] = []

    def add_component(self, component: FileSystemComponent) -> None:
        """
        Add a file system component to the directory.
        """
        self.children.append(component)

    def remove_component(self, component: FileSystemComponent) -> None:
        """
        Remove a file system component from the directory.
        """
        self.children.remove(component)

    def display_details(self) -> None:
        """
        Display details of the directory and its contents recursively.
        """
        print(f"Directory: {self.name}")
        print("Contents:")
        for component in self.children:
            component.display_details()


# Client code
if __name__ == '__main__':
    # Create files
    file1 = File("Document.txt")
    file2 = File("Image.jpg")
    file3 = File("Spreadsheet.xlsx")

    # Create directories
    directory1 = Directory("Documents")
    directory1.add_component(file1)
    directory1.add_component(file3)

    directory2 = Directory("Pictures")
    directory2.add_component(file2)

    root_directory = Directory("Root")
    root_directory.add_component(directory1)
    root_directory.add_component(directory2)

    # Display details of the entire file system
    root_directory.display_details()
    