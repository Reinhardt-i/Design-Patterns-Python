from abc import ABC, abstractmethod

# 1. State interface
class PackageState(ABC):
    @abstractmethod
    def next(self, delivery_package: 'DeliveryPackage') -> None:
        pass

    @abstractmethod
    def prev(self, delivery_package: 'DeliveryPackage') -> None:
        pass

    @abstractmethod
    def print_status(self) -> None:
        pass


# Concrete states
class OrderedState(PackageState):
    def next(self, delivery_package: 'DeliveryPackage') -> None:
        delivery_package.set_state(DeliveredState())

    def prev(self, delivery_package: 'DeliveryPackage') -> None:
        print("The package is in its root state.")

    def print_status(self) -> None:
        print("Package ordered, not delivered to the office yet.")


class DeliveredState(PackageState):
    def next(self, delivery_package: 'DeliveryPackage') -> None:
        delivery_package.set_state(ReceivedState())

    def prev(self, delivery_package: 'DeliveryPackage') -> None:
        delivery_package.set_state(OrderedState())

    def print_status(self) -> None:
        print("Package delivered to post office, not received yet.")


class ReceivedState(PackageState):
    def next(self, delivery_package: 'DeliveryPackage') -> None:
        print("This package is already received by a client.")

    def prev(self, delivery_package: 'DeliveryPackage') -> None:
        delivery_package.set_state(DeliveredState())

    def print_status(self) -> None:
        print("Package is successfully received by the client!!")


# Context class
class DeliveryPackage:
    def __init__(self):
        self._state: PackageState = OrderedState()

    def set_state(self, state: PackageState) -> None:
        self._state = state

    def next_state(self) -> None:
        self._state.next(self)

    def previous_state(self) -> None:
        self._state.prev(self)

    def print_status(self) -> None:
        self._state.print_status()


# Usage
if __name__ == '__main__':
    # Create a delivery package instance
    delivery_package = DeliveryPackage()

    # Initial state
    delivery_package.print_status()

    # Transition to the next state
    delivery_package.next_state()
    delivery_package.print_status()

    # Transition to the next state again
    delivery_package.next_state()
    delivery_package.print_status()

    # Transition to the next state once more
    delivery_package.next_state()
    