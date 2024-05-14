from abc import ABC, abstractmethod
from typing import List


class FileSystemComponent(ABC):
    """Abstract base class for file system components."""
    
    @abstractmethod
    def get_size(self) -> int:
        """Returns the size of the component."""
        pass


class File(FileSystemComponent):
    """Concrete class representing a file."""
    
    def __init__(self, name: str, size: int) -> None:
        """Initializes the file with a name and size."""
        self.name = name
        self.size = size

    def get_size(self) -> int:
        """Returns the size of the file."""
        return self.size


class Directory(FileSystemComponent):
    """Concrete class representing a directory."""
    
    def __init__(self, name: str) -> None:
        """Initializes the directory with a name."""
        self.name = name
        self.children: List[FileSystemComponent] = []

    def add_component(self, component: FileSystemComponent) -> None:
        """Adds a component to the directory."""
        self.children.append(component)

    def remove_component(self, component: FileSystemComponent) -> None:
        """Removes a component from the directory."""
        self.children.remove(component)

    def get_size(self) -> int:
        """Returns the total size of the directory and its components."""
        total_size = 0
        for component in self.children:
            total_size += component.get_size()
        return total_size


if __name__ == '__main__':
    # Creating files
    file1 = File("Bijon_CV.pdf", 120)
    file2 = File("Priyo_mymensing.jpg", 200)
    file3 = File("Video.mp4", 1500)
    file4 = File("swe_secrets.txt", 500)
    file5 = File("dp_notes_in_python.md", 420)

    # Creating directories
    directory1 = Directory("Docs")
    directory1.add_component(file1)
    directory1.add_component(file4)
    directory1.add_component(file5)

    directory2 = Directory("Pics and Vids")
    directory2.add_component(file2)
    directory2.add_component(file3)

    root_directory = Directory("Root")
    root_directory.add_component(directory1)
    root_directory.add_component(directory2)

    # Displaying size of the entire file system
    print(f"Total size of '{root_directory.name}' directory = {root_directory.get_size()} bytes")
