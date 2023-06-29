class Circle:
    def __init__(self, x: int = 0, y: int = 0, radius: int = 0):
        self._x = x
        self._y = y
        self._radius = radius

    def draw(self) -> None:
        print(f"Circle drawn on ({self._x}, {self._y}), Radius: {self._radius}")

    def clone(self) -> 'Circle':
        return Circle(self._x, self._y, self._radius)


if __name__ == '__main__':
    # Create a circle
    c1 = Circle(10, 20, 5)
    c1.color = "Red"

    # Trying to copy c2 into c1
    c2 = c1.clone()
    c2.draw()
    