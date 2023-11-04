import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def is_valid(self):
        # Перевірка на існування трикутника за нерівністю трикутника
        a = self.point1.distance_to(self.point2)
        b = self.point2.distance_to(self.point3)
        c = self.point3.distance_to(self.point1)
        return (a + b > c) and (b + c > a) and (c + a > b)

    def perimeter(self):
        if self.is_valid():
            a = self.point1.distance_to(self.point2)
            b = self.point2.distance_to(self.point3)
            c = self.point3.distance_to(self.point1)
            return a + b + c
        else:
            return None

    def area(self):
        if self.is_valid():
            a = self.point1.distance_to(self.point2)
            b = self.point2.distance_to(self.point3)
            c = self.point3.distance_to(self.point1)
            s = 0.5 * self.perimeter()
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        else:
            return None

point1 = Point(0, 0)
point2 = Point(3, 0)
point3 = Point(0, 4)

triangle = Triangle(point1, point2, point3)
if triangle.is_valid():
    print(f"Периметр трикутника: {triangle.perimeter()}")
    print(f"Площа трикутника: {triangle.area()}")
else:
    print("Такий трикутник не існує.")
