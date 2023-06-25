class Database:
    _database_instance = None  # The single instance of the Database class

    def __init__(self, username):
        self._username = username

    @staticmethod
    def get_database_instance(username):
        if Database._database_instance is None:  # Check if the instance has been created
            Database._database_instance = Database(username)  # If not, create a new instance
        return Database._database_instance  # Return the instance (either newly created or existing)

    def get_username(self):
        return self._username  # Return the username associated with the instance


# Usage
if __name__ == '__main__':
    # Creating the first database session
    session1 = Database.get_database_instance("Avik")
    print(session1.get_username())

    # Trying to create another database session
    # Note: The same instance will be returned as per the Singleton pattern
    session2 = Database.get_database_instance("Mahir")
    print(session2.get_username())
    