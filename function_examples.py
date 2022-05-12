from math import pi
# import typing

def hello():
    print("Hello, world")

hello()
hello()

def circle_area(diameter):
    radius = diameter / 2
    return pi * (radius ** 2)

a1 = circle_area(10)
a2 = circle_area(3.7)
a3 = circle_area(2)
print(a1, a2, a3)


def animal():
    return "wombat"

x = animal()
print(x)

# print(circle_area("hello"))

def rectangle_area(length, width):
    return length * width

a1 = rectangle_area(5, 10)
a2 = rectangle_area(32, 68)
print(a1, a2)


def greet(whom="world"): # default value for parameter
    print("Hello,", whom)

greet()
greet("New York")
greet("Dolly")







