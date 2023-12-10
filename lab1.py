import math

class Line:
    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

    def intersection_point(self, other_line):
        # Вычисление точки пересечения двух прямых
        x = (other_line.intercept - self.intercept) / (self.slope - other_line.slope)
        y = self.slope * x + self.intercept
        return x, y

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def does_intersect(self, other_circle):
        # Проверка пересечения двух окружностей
        distance = math.sqrt((self.center_x - other_circle.center_x)**2 + (self.center_y - other_circle.center_y)**2)
        return distance < self.radius + other_circle.radius

class GeometryHandler:
    def __init__(self):
        self.lines = []
        self.circles = []

    def add_line(self, slope, intercept):
        self.lines.append(Line(slope, intercept))

    def add_circle(self, center_x, center_y, radius):
        self.circles.append(Circle(center_x, center_y, radius))

    def print_intersections(self):
        # Вывод пересечений прямых и окружностей
        for i, line1 in enumerate(self.lines):
            for j, line2 in enumerate(self.lines[i+1:]):
                intersection = line1.intersection_point(line2)
                print(f"Intersection Point of Lines {i+1} and {i+1+j+1}: {intersection}")

        for i, circle1 in enumerate(self.circles):
            for j, circle2 in enumerate(self.circles[i+1:]):
                does_intersect = circle1.does_intersect(circle2)
                print(f"Do Circles {i+1} and {i+1+j+1} Intersect: {does_intersect}")

# Пример использования
geometry_handler = GeometryHandler()
geometry_handler.add_line(slope=2, intercept=1)
geometry_handler.add_line(slope=-1, intercept=3)
geometry_handler.add_circle(center_x=0, center_y=0, radius=3)
geometry_handler.add_circle(center_x=4, center_y=0, radius=3)

geometry_handler.print_intersections()
