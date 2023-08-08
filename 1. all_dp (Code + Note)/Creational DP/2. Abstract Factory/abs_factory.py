from abc import ABC, abstractmethod


# Abstract Product: Asteroids
class AbstractAsteroid(ABC):
    @abstractmethod
    def show(self) -> None:
        pass


# Concrete Products: IceAsteroid, IronAsteroid, RockyAsteroid, SiliconAsteroid, DiamondAsteroid, GoldAsteroid, CrystalAsteroid
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


class DiamondAsteroid(AbstractAsteroid):
    def show(self) -> None:
        print("Diamond Asteroid popped up")


class GoldAsteroid(AbstractAsteroid):
    def show(self) -> None:
        print("Gold Asteroid popped up")


class CrystalAsteroid(AbstractAsteroid):
    def show(self) -> None:
        print("Crystal Asteroid popped up")


# Abstract Product: Debris Fields
class AbstractDebrisField(ABC):
    @abstractmethod
    def show(self) -> None:
        pass


# Concrete Products: DynamicDebrisField, PersistentDebrisField, StaticDebrisField, ExplosiveDebrisField, MagneticDebrisField, ToxicDebrisField
class DynamicDebrisField(AbstractDebrisField):
    def show(self) -> None:
        print("Dynamic Debris Field appeared")


class PersistentDebrisField(AbstractDebrisField):
    def show(self) -> None:
        print("Persistent Debris Field appeared")


class StaticDebrisField(AbstractDebrisField):
    def show(self) -> None:
        print("Static Debris Field appeared")


class ExplosiveDebrisField(AbstractDebrisField):
    def show(self) -> None:
        print("Explosive Debris Field appeared")


class MagneticDebrisField(AbstractDebrisField):
    def show(self) -> None:
        print("Magnetic Debris Field appeared")


class ToxicDebrisField(AbstractDebrisField):
    def show(self) -> None:
        print("Toxic Debris Field appeared")


# Abstract Factory: ObstacleFactory
class ObstacleFactory(ABC):
    @abstractmethod
    def create_asteroid(self) -> AbstractAsteroid:
        pass

    @abstractmethod
    def create_debris_field(self) -> AbstractDebrisField:
        pass


# Concrete Factories: Level1Factory, Level2Factory, Level3Factory, Level4Factory, Level5Factory
class Level1Factory(ObstacleFactory):
    def create_asteroid(self) -> AbstractAsteroid:
        return IceAsteroid()

    def create_debris_field(self) -> AbstractDebrisField:
        return StaticDebrisField()


class Level2Factory(ObstacleFactory):
    def create_asteroid(self) -> AbstractAsteroid:
        return SiliconAsteroid()

    def create_debris_field(self) -> AbstractDebrisField:
        return DynamicDebrisField()


class Level3Factory(ObstacleFactory):
    def create_asteroid(self) -> AbstractAsteroid:
        return DiamondAsteroid()

    def create_debris_field(self) -> AbstractDebrisField:
        return ExplosiveDebrisField()


class Level4Factory(ObstacleFactory):
    def create_asteroid(self) -> AbstractAsteroid:
        return GoldAsteroid()

    def create_debris_field(self) -> AbstractDebrisField:
        return MagneticDebrisField()


class Level5Factory(ObstacleFactory):
    def create_asteroid(self) -> AbstractAsteroid:
        return CrystalAsteroid()

    def create_debris_field(self) -> AbstractDebrisField:
        return ToxicDebrisField()


# Client
if __name__ == "__main__":
    import random

    # Randomly select a level
    level = random.randint(1, 5)

    # Randomly generate a score
    score = random.randint(0, 2000)

    # Instantiate the appropriate factory based on the level
    if level == 1:
        factory = Level1Factory()
    elif level == 2:
        factory = Level2Factory()
    elif level == 3:
        factory = Level3Factory()
    elif level == 4:
        factory = Level4Factory()
    else:
        factory = Level5Factory()

    # Create an asteroid using the factory
    asteroid = factory.create_asteroid()
    asteroid.show()

    # Create a debris field using the factory
    debris_field = factory.create_debris_field()
    debris_field.show()
