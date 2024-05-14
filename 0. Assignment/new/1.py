from abc import ABC, abstractmethod


class Pizza(ABC):
    """Abstract base class for Pizza."""
    
    @abstractmethod
    def get_description(self) -> str:
        """Returns the description of the pizza."""
        pass

    @abstractmethod
    def get_cost(self) -> float:
        """Returns the cost of the pizza."""
        pass


class PlainPizza(Pizza):
    """Concrete class representing a plain pizza."""
    
    def get_description(self) -> str:
        """Returns the description of a plain pizza."""
        return "Plain Pizza"

    def get_cost(self) -> float:
        """Returns the cost of a plain pizza."""
        return 4.0


class PizzaDecorator(Pizza, ABC):
    """Abstract decorator class for Pizza."""
    
    def __init__(self, decorated_pizza: Pizza) -> None:
        """Initializes the decorator with a pizza to decorate."""
        self.decorated_pizza = decorated_pizza

    def get_description(self) -> str:
        """Returns the description of the decorated pizza."""
        return self.decorated_pizza.get_description()

    def get_cost(self) -> float:
        """Returns the cost of the decorated pizza."""
        return self.decorated_pizza.get_cost()


class CheeseDecorator(PizzaDecorator):
    """Concrete decorator class adding cheese to a pizza."""
    
    def get_description(self) -> str:
        """Returns the description of the pizza with cheese."""
        return super().get_description() + ", added: Cheese"

    def get_cost(self) -> float:
        """Returns the cost of the pizza with cheese."""
        return super().get_cost() + 1.5


class PepperoniDecorator(PizzaDecorator):
    """Concrete decorator class adding pepperoni to a pizza."""
    
    def get_description(self) -> str:
        """Returns the description of the pizza with pepperoni."""
        return super().get_description() + ", Pepperoni"

    def get_cost(self) -> float:
        """Returns the cost of the pizza with pepperoni."""
        return super().get_cost() + 2.0


class BeefDecorator(PizzaDecorator):
    """Concrete decorator class adding beef to a pizza."""
    
    def get_description(self) -> str:
        """Returns the description of the pizza with beef."""
        return super().get_description() + ", Beef"

    def get_cost(self) -> float:
        """Returns the cost of the pizza with beef."""
        return super().get_cost() + 2.5


if __name__ == '__main__':
    
    pizza = PlainPizza()  # Creating a plain pizza
    print(pizza.get_description(), "Cost: $", pizza.get_cost())
    
    pizza_with_cheese = CheeseDecorator(pizza)  # Decorating the pizza with cheese
    print(pizza_with_cheese.get_description(), "Cost: $", pizza_with_cheese.get_cost())

    pizza_with_cheese_and_pepperoni = PepperoniDecorator(pizza_with_cheese)  # Adding pepperoni to the cheese pizza
    print(pizza_with_cheese_and_pepperoni.get_description(), "Cost: $", pizza_with_cheese_and_pepperoni.get_cost())
    
    beef_pizza_with_cheese_and_pepperoni = BeefDecorator(pizza_with_cheese_and_pepperoni)  # Adding beef to the cheese and pepperoni pizza
    print(beef_pizza_with_cheese_and_pepperoni.get_description(), "Cost: $", beef_pizza_with_cheese_and_pepperoni.get_cost())

