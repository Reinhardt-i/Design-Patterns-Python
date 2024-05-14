from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract base class for commands."""
    
    @abstractmethod
    def execute(self) -> None:
        """Executes the command."""
        pass


class CreateFileCommand(Command):
    """Concrete command to create a file."""
    
    def execute(self) -> None:
        """Executes the create file command."""
        print("touch x : file created")


class DeleteFileCommand(Command):
    """Concrete command to delete a file."""
    
    def execute(self) -> None:
        """Executes the delete file command."""
        print("rm -rf : file deleted")


class RenameFileCommand(Command):
    """Concrete command to rename a file."""
    
    def execute(self) -> None:
        """Executes the rename file command."""
        print("mv oldname newname : file renamed")


class CommandExecutor:
    """Invoker class to execute commands based on user role."""
    
    def __init__(self, role: str) -> None:
        """Initializes the command executor with a user role."""
        self.role = role
        self.commands = {
            "create": CreateFileCommand(),
            "delete": DeleteFileCommand(),
            "rename": RenameFileCommand(),
        }

    def execute_command(self, command_name: str) -> None:
        """Executes the specified command if permitted."""
        if command_name == "delete" and self.role != "admin":
            print("Access denied: Only admin can execute 'delete' command")
        elif command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"Command '{command_name}' not recognized")



if __name__ == '__main__':
    print("Admin commands: ")
    admin_executor = CommandExecutor(role="admin")
    admin_executor.execute_command("create")
    admin_executor.execute_command("delete")
    admin_executor.execute_command("rename")
    print("\n\n")

    print("Normal User commands: ")
    user_executor = CommandExecutor(role="normal_user")
    user_executor.execute_command("create")
    user_executor.execute_command("delete")
    user_executor.execute_command("rename")
    print("\n\n")
