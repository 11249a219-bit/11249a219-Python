AIM:
To write a python program to find the area of triangle, circle and rectangle by using the
concept of inheritance.
ALGORITHM:
1. Start
2. Define a base class Shape with a method area() (can be an empty or general method).
3. Define a derived class Triangle that inherits from Shape:
a) Take base and height as input
b) Implement the area() method as: (0.5 * base * height)
4. Define a derived class Rectangle that inherits from Shape:
a) Take length and width as input
b) Implement the area() method as: length * width
5. Define a derived class Circle that inherits from Shape:
a) Take radius as input
b) Implement the area() method as: π * radius^2
6. Create instances of each derived class and call the area() method
7. Display the results
8. End
PROGRAM:
import math
# Base Class
class Shape:
def area(self):
return 0
# Derived Class for Triangle
class Triangle(Shape):
def __init__(self, base, height):
self.base = base
self.height = height
def area(self):
return 0.5 * self.base * self.height
# Derived Class for Rectangle
class Rectangle(Shape):
def __init__(self, length, width):
self.length = length
self.width = width
def area(self):
return self.length * self.width
# Derived Class for Circle
class Circle(Shape):
def __init__(self, radius):
self.radius = radius
def area(self):
return math.pi * self.radius ** 2
# Main Program
print("Area Calculations:")
# Triangle
b = float(input("Enter base of triangle: "))
h = float(input("Enter height of triangle: "))
triangle = Triangle(b, h)
print(f"Area of Triangle: {triangle.area():.2f}")
# Rectangle
l = float(input("\nEnter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
rectangle = Rectangle(l, w)
print(f"Area of Rectangle: {rectangle.area():.2f}")
# Circle
r = float(input("\nEnter radius of circle: "))
circle = Circle(r)
print(f"Area of Circle: {circle.area():.2f}")
OUTPUT:
Area Calculations:
Enter base of triangle: 10
Enter height of triangle: 5
Area of Triangle: 25.00
Enter length of rectangle: 8
Enter width of rectangle: 4
Area of Rectangle: 32.00
Enter radius of circle: 7
Area of Circle: 153.94
