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


# Concrete 2. Factory for Level 2
class Level2AsteroidsFactory(AsteroidsFactory):
    def create_asteroids(self, score: int) -> "Asteroids":
        """
        Create asteroids for Level 2 based on the score.
        """
        if score > 1000:
            return RockyAsteroids()
        else:
            return SiliconAsteroids()
        


# New Concrete 3. Factory for Level 3
class Level3AsteroidsFactory(AsteroidsFactory):
    def create_asteroids(self, score: int) -> "Asteroids":
        """
        Create asteroids for Level 3 based on the score.
        """
        if score > 2000:
            return FireAsteroids()
        else:
            return DiamondAsteroids()


# New Concrete 4. Factory for Level 4
class Level4AsteroidsFactory(AsteroidsFactory):
    def create_asteroids(self, score: int) -> "Asteroids":
        """
        Create asteroids for Level 4 based on the score.
        """
        if score > 3000:
            return MagneticAsteroids()
        else:
            return FireAsteroids()



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


# New Concrete Product: Fire Asteroids
class FireAsteroids(Asteroids):
    def show(self) -> None:
        """
        Show message for Fire Asteroids.
        """
        print("Fire_Asteroids popped up")


# New Concrete Product: Diamond Asteroids
class DiamondAsteroids(Asteroids):
    def show(self) -> None:
        """
        Show message for Diamond Asteroids.
        """
        print("Diamond_Asteroids popped up")


# New Concrete Product: Magnetic Asteroids
class MagneticAsteroids(Asteroids):
    def show(self) -> None:
        """
        Show message for Magnetic Asteroids.
        """
        print("Magnetic_Asteroids popped up")



if __name__ == "__main__":
    
    level = random.randint(1, 4)
    score = random.randint(0, 4000)

    # Create the appropriate factory based on the level
    if level == 1:
        asteroids_factory: AsteroidsFactory = Level1AsteroidsFactory()
    elif level == 2:
        asteroids_factory: AsteroidsFactory = Level2AsteroidsFactory()
    elif level == 3:
        asteroids_factory: AsteroidsFactory = Level3AsteroidsFactory()
    else:
        asteroids_factory: AsteroidsFactory = Level4AsteroidsFactory()

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
