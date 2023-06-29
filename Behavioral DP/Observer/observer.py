from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    """
    The Subject interface declares the methods for managing observers.
    """

    @abstractmethod
    def attach(self, observer: 'Observer') -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: 'Observer') -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """
        Notify all observers about a state change.
        """
        pass


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects to notify observers.
    """

    @abstractmethod
    def update(self, temperature: float) -> None:
        """
        Receive an update from the subject.
        """
        pass


class WeatherStation(Subject):
    """
    The WeatherStation class implements the Subject interface and tracks the temperature.
    It maintains a list of observers and notifies them when the temperature changes.
    """

    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature: float = 0.0

    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the weather station.
        """
        print(f"Attached an observer: {observer.__class__.__name__}")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the weather station.
        """
        print(f"Detached an observer: {observer.__class__.__name__}")
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        """
        Notify all observers about a temperature change.
        """
        print("Notifying observers...")
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float) -> None:
        """
        Set the temperature and notify observers.
        """
        print(f"Temperature changed to: {temperature}")
        self._temperature = temperature
        self.notify_observers()


class User(Observer):
    """
    The User class implements the Observer interface and receives updates from the weather station.
    """

    def __init__(self, name: str):
        self._name = name

    def update(self, temperature: float) -> None:
        """
        Receive an update from the weather station.
        """
        print(f"{self._name} received an update: Temperature is {temperature}")


if __name__ == "__main__":
    # Create weather station and users
    weather_station = WeatherStation()
    user1 = User("John")
    user2 = User("Emily")
    user3 = User("David")

    # Attach users to the weather station
    weather_station.attach(user1)
    weather_station.attach(user2)
    weather_station.attach(user3)

    # Set the temperature and notify observers
    weather_station.set_temperature(25.5)
    # Output: John received an update: Temperature is 25.5
    #         Emily received an update: Temperature is 25.5
    #         David received an update: Temperature is 25.5

    # Detach an observer from the weather station
    weather_station.detach(user2)

    # Set a new temperature and notify observers
    weather_station.set_temperature(30.0)
    # Output: John received an update: Temperature is 30.0
    #         David received an update: Temperature is 30.0
    