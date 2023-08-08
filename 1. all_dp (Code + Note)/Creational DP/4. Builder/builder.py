"""
Creating a Burger using the Builder Pattern

The Builder pattern is a creational design pattern that separates the construction of complex objects from their representation,
allowing the same construction process to create different representations. In this example, we demonstrate how to create a burger
using the Builder pattern.

1. Burger Class:
    - The `Burger` class represents the final product with various attributes such as size, patty, cheese, tomatoes, lettuce, onions, and pickles.
    - It provides methods like `has_patty()`, `has_cheese()`, etc., to check the presence of specific ingredients in the burger.
    - The `__str__` method is overridden to provide a human-readable representation of the burger's details.

2. BurgerBuilder Class:
    - The `BurgerBuilder` class is responsible for constructing the burger step by step.
    - It initializes with the burger's size and default values for all ingredients (set to False).
    - The class provides methods like `add_patty()`, `add_cheese()`, etc., to set the corresponding ingredient to True.
    - Each method returns `self`, enabling method chaining for a fluent and expressive way to build the burger.
    - The `build()` method creates the `Burger` object by passing itself (`self`) to the `Burger` constructor.

3. Usage:
    - In the `__main__` section, we demonstrate the construction of a burger using the `BurgerBuilder` class.
    - We start by specifying the burger's size (e.g., "regular").
    - Then, we chain the `add_patty()`, `add_cheese()`, etc., methods to select the desired ingredients for the burger.
    - Finally, we call the `build()` method to get the final `Burger` object.
    - The `__str__` method of the `Burger` class provides a human-readable representation of the burger's details, including its size and the selected ingredients.

Using the Builder pattern allows us to create a burger with different combinations of ingredients in a clear and maintainable way.
"""


class Pizza:
    def __init__(self, builder):
        self.size = builder.size
        self.cheese = builder.cheese
        self.pepperoni = builder.pepperoni
        self.mushrooms = builder.mushrooms
        self.onions = builder.onions
        self.tomatoes = builder.tomatoes
        self.crust_type = builder.crust_type

    # The next methods are for checking only, pattern e kono dorkar nai tbh.
    def is_cheese(self) -> bool:
        return self.cheese

    def is_pepperoni(self) -> bool:
        return self.pepperoni

    def is_mushrooms(self) -> bool:
        return self.mushrooms

    def is_onions(self) -> bool:
        return self.onions

    def is_tomatoes(self) -> bool:
        return self.tomatoes

    def get_crust_type(self) -> str:
        return self.crust_type

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("Cheese")
        if self.pepperoni:
            toppings.append("Pepperoni")
        if self.mushrooms:
            toppings.append("Mushrooms")
        if self.onions:
            toppings.append("Onions")
        if self.tomatoes:
            toppings.append("Tomatoes")

        return f"Size: {self.size}, Crust Type: {self.crust_type}, Toppings: {', '.join(toppings)}"


class PizzaBuilder:
    def __init__(self, size: str):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.tomatoes = False
        self.crust_type = "regular"

    def add_cheese(self, cheese: bool) -> 'PizzaBuilder':
        self.cheese = cheese
        return self

    def add_pepperoni(self, pepperoni: bool) -> 'PizzaBuilder':
        self.pepperoni = pepperoni
        return self

    def add_mushrooms(self, mushrooms: bool) -> 'PizzaBuilder':
        self.mushrooms = mushrooms
        return self

    def add_onions(self, onions: bool) -> 'PizzaBuilder':
        self.onions = onions
        return self

    def add_tomatoes(self, tomatoes: bool) -> 'PizzaBuilder':
        self.tomatoes = tomatoes
        return self

    def set_crust_type(self, crust_type: str) -> 'PizzaBuilder':
        self.crust_type = crust_type
        return self

    def build(self) -> Pizza:
        return Pizza(self)



if __name__ == '__main__':
    pizza = PizzaBuilder("larger") \
            .add_cheese(True) \
            .add_onions(True) \
            .add_tomatoes(True) \
            .set_crust_type("thin") \
            .build()

    print(pizza)
