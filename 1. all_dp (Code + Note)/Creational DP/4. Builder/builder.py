class Pizza:
    def __init__(self, builder):
        self.size = builder.size
        self.cheese = builder.cheese
        self.pepperoni = builder.pepperoni
        self.mushrooms = builder.mushrooms
        self.onions = builder.onions

    # The next methods are for checking only, pattern e kono dorkar nai tbh.
    def is_cheese(self) -> bool:
        return self.cheese

    def is_pepperoni(self) -> bool:
        return self.pepperoni

    def is_mushrooms(self) -> bool:
        return self.mushrooms

    def is_onions(self) -> bool:
        return self.onions


class PizzaBuilder:
    def __init__(self, size: str):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False

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

    def build(self) -> Pizza:
        return Pizza(self)


# Usage
if __name__ == '__main__':
    pizza = PizzaBuilder("larger") \
            .add_cheese(True) \
            .add_onions(True) \
            .build()

    print(pizza.is_cheese())
    print(pizza.is_onions())
    print(pizza.is_mushrooms())
    