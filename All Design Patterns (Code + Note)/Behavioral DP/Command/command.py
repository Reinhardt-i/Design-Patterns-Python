from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares the method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Executes the command.
        """
        pass


class OpenFileCommand(Command):
    """
    The OpenFileCommand is a concrete command that opens a file using the FileManager.
    """

    def __init__(self, file_manager: 'FileManager') -> None:
        self.file_manager = file_manager

    def execute(self) -> None:
        self.file_manager.open_file()


class SaveFileCommand(Command):
    """
    The SaveFileCommand is a concrete command that saves a file using the FileManager.
    """

    def __init__(self, file_manager: 'FileManager') -> None:
        self.file_manager = file_manager

    def execute(self) -> None:
        self.file_manager.save_file()


class FileManager:
    """
    The FileManager acts as the receiver and performs the actual operations.
    """

    def open_file(self) -> None:
        print("File opened")

    def save_file(self) -> None:
        print("File saved")


class FileInvoker:
    """
    The FileInvoker acts as the invoker and executes commands.
    """

    def __init__(self) -> None:
        self.command = None

    def set_command(self, command: Command) -> None:
        """
        Sets the command to be executed.
        """
        self.command = command

    def execute_command(self) -> None:
        """
        Executes the command.
        """
        self.command.execute()


def main() -> None:
    """
    The main function demonstrates the Command pattern usage.
    """
    file_invoker = FileInvoker()
    file_manager = FileManager()

    open_file_command = OpenFileCommand(file_manager)
    save_file_command = SaveFileCommand(file_manager)

    file_invoker.set_command(open_file_command)
    file_invoker.execute_command()

    file_invoker.set_command(save_file_command)
    file_invoker.execute_command()


if __name__ == '__main__':
    main()
    