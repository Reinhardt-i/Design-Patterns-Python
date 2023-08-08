import random


# Abstract 1. Factory
class AsteroidsFactory:
    def create_asteroids(self, score: int) -> "Asteroids":
        """
        Abstract method for creating asteroids based on the score.
        """
        raise NotImplementedError


# Concrete 1. Factory for Level 1
class Level1AsteroidsFactory(AsteroidsFactory):
    def create_asteroids(self, score: int) -> "Asteroids":
        """
        Create asteroids for Level 1 based on the score.
        """
        if score > 500:
            return IceAsteroids()
        else:
            return IronAsteroids()


# Concrete 1. Factory for Level 2
class Level2AsteroidsFactory(AsteroidsFactory):
    def create_asteroids(self, score: int) -> "Asteroids":
        """
        Create asteroids for Level 2 based on the score.
        """
        if score > 1000:
            return RockyAsteroids()
        else:
            return SiliconAsteroids()


# Product Interface
class Asteroids:
    def show(self) -> None:
        """
        Abstract method to show the type of asteroids.
        """
        raise NotImplementedError


# Concrete Product: Ice Asteroids
class IceAsteroids(Asteroids):
    def show(self) -> None:
        """
        Show message for Ice Asteroids.
        """
        print("Ice_Asteroids popped up")


# Concrete Product: Iron Asteroids
class IronAsteroids(Asteroids):
    def show(self) -> None:
        """
        Show message for Iron Asteroids.
        """
        print("Iron_Asteroids popped up")


# Concrete Product: Rocky Asteroids
class RockyAsteroids(Asteroids):
    def show(self) -> None:
        """
        Show message for Rocky Asteroids.
        """
        print("Rocky_Asteroids popped up")


# Concrete Product: Silicon Asteroids
class SiliconAsteroids(Asteroids):
    def show(self) -> None:
        """
        Show message for Silicon Asteroids.
        """
        print("Silicon_Asteroids popped up")


if __name__ == "__main__":
    level = random.randint(1, 2)
    score = random.randint(0, 2000)

    # Create the appropriate factory based on the level
    if level == 1:
        asteroids_factory: AsteroidsFactory = Level1AsteroidsFactory()
    else:
        asteroids_factory: AsteroidsFactory = Level2AsteroidsFactory()

    # Create asteroids based on the score using the factory
    asteroids: Asteroids = asteroids_factory.create_asteroids(score)

    # Show the type of asteroids that popped up
    asteroids.show()
    
    
# The abstract class AsteroidsFactory defines the factory interface, and the concrete factories
# Level1AsteroidsFactory and Level2AsteroidsFactory implement the creation logic for each level.
# The Asteroids interface represents the product, and the concrete classes IceAsteroids, IronAsteroids,
# RockyAsteroids, and SiliconAsteroids are the concrete implementations of the products.

# In the Client code, a random level and score are generated. The appropriate factory is chosen based
# on the level, and the factory's create_asteroids method is called to create an instance of the
# Asteroids product. Finally, the show method is invoked to display the message indicating the type of
# asteroids that popped up.
