from abc import ABC, abstractmethod


# Abstract Product: Asteroids
class AbstractAsteroid(ABC):
    @abstractmethod
    def show(self) -> None:
        pass


# Concrete Products: IceAsteroid, IronAsteroid, RockyAsteroid, SiliconAsteroid
class IceAsteroid(AbstractAsteroid):
    def show(self) -> None:
        print("Ice Asteroid popped up")


class IronAsteroid(AbstractAsteroid):
    def show(self) -> None:
        print("Iron Asteroid popped up")


class RockyAsteroid(AbstractAsteroid):
    def show(self) -> None:
        print("Rocky Asteroid popped up")


class SiliconAsteroid(AbstractAsteroid):
    def show(self) -> None:
        print("Silicon Asteroid popped up")


# Abstract Product: Debris Fields
class AbstractDebrisField(ABC):
    @abstractmethod
    def show(self) -> None:
        pass


# Concrete Products: DynamicDebrisField, PersistentDebrisField, StaticDebrisField
class DynamicDebrisField(AbstractDebrisField):
    def show(self) -> None:
        print("Dynamic Debris Field appeared")


class PersistentDebrisField(AbstractDebrisField):
    def show(self) -> None:
        print("Persistent Debris Field appeared")


class StaticDebrisField(AbstractDebrisField):
    def show(self) -> None:
        print("Static Debris Field appeared")


# Abstract Factory: ObstacleFactory
class ObstacleFactory(ABC):
    @abstractmethod
    def create_asteroid(self) -> AbstractAsteroid:
        pass

    @abstractmethod
    def create_debris_field(self) -> AbstractDebrisField:
        pass


# Concrete Factory: Level1Factory
class Level1Factory(ObstacleFactory):
    def create_asteroid(self) -> AbstractAsteroid:
        return IceAsteroid()

    def create_debris_field(self) -> AbstractDebrisField:
        return StaticDebrisField()


# Concrete Factory: Level2Factory
class Level2Factory(ObstacleFactory):
    def create_asteroid(self) -> AbstractAsteroid:
        return SiliconAsteroid()

    def create_debris_field(self) -> AbstractDebrisField:
        return DynamicDebrisField()


# Client
if __name__ == "__main__":
    import random

    # Randomly select a level
    level = random.randint(1, 2)

    # Randomly generate a score
    score = random.randint(0, 2000)

    # Instantiate the appropriate factory based on the level
    if level == 1:
        factory = Level1Factory()
    else:
        factory = Level2Factory()

    # Create an asteroid using the factory
    asteroid = factory.create_asteroid()
    asteroid.show()

    # Create a debris field using the factory
    debris_field = factory.create_debris_field()
    debris_field.show()
    