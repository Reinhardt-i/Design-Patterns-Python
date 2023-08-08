from abc import ABC, abstractmethod


class Pizza(ABC):
    """
    Pizza interface that defines the methods to be implemented by concrete pizzas.
    """

    @abstractmethod
    def get_description(self) -> str:
        """
        Returns the description of the pizza.
        """
        pass

    @abstractmethod
    def get_cost(self) -> float:
        """
        Returns the cost of the pizza.
        """
        pass


class PlainPizza(Pizza):
    """
    Concrete component class representing a plain pizza.
    """

    def get_description(self) -> str:
        return "Plain Pizza"

    def get_cost(self) -> float:
        return 4.0


class PizzaDecorator(Pizza, ABC):
    """
    Abstract decorator class that implements the Pizza interface.
    """

    def __init__(self, decorated_pizza: Pizza):
        self.decorated_pizza = decorated_pizza

    def get_description(self) -> str:
        return self.decorated_pizza.get_description()

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost()


class CheeseDecorator(PizzaDecorator):
    """
    Concrete decorator class adding cheese topping to a pizza.
    """

    def get_description(self) -> str:
        return super().get_description() + ", Cheese"

    def get_cost(self) -> float:
        return super().get_cost() + 1.5


class PepperoniDecorator(PizzaDecorator):
    """
    Concrete decorator class adding pepperoni topping to a pizza.
    """

    def get_description(self) -> str:
        return super().get_description() + ", Pepperoni"

    def get_cost(self) -> float:
        return super().get_cost() + 2.0


if __name__ == '__main__':
    # Create a plain pizza
    pizza = PlainPizza()
    print(pizza.get_description(), "Cost: $", pizza.get_cost())

    # Add cheese to the pizza using a decorator
    pizza_with_cheese = CheeseDecorator(pizza)
    print(pizza_with_cheese.get_description(), "Cost: $", pizza_with_cheese.get_cost())

    # Add pepperoni to the pizza using a decorator
    pizza_with_cheese_and_pepperoni = PepperoniDecorator(pizza_with_cheese)
    print(
        pizza_with_cheese_and_pepperoni.get_description(),
        "Cost: $",
        pizza_with_cheese_and_pepperoni.get_cost()
    )
    