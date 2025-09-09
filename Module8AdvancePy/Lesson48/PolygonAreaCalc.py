import math

class Calculator:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def __str__(self):
        return f"{self.name} with area: {self.area():.2f}"


class Triangle(Calculator):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Rectangle(Calculator):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class RegularPolygon(Calculator):
    def __init__(self, num_sides, side_length):
        if num_sides < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        super().__init__(f"Regular Polygon with {num_sides} sides")
        self.num_sides = num_sides
        self.side_length = side_length

    def area(self):
        n = self.num_sides
        s = self.side_length
        return (n * s ** 2) / (4 * math.tan(math.pi / n))


# Example usage
if __name__ == "__main__":
    triangle = Triangle(base=10, height=5)
    print(triangle)

    rectangle = Rectangle(width=8, height=4)
    print(rectangle)

    regular_polygon = RegularPolygon(num_sides=6, side_length=4)  # Hexagon
    print(regular_polygon)