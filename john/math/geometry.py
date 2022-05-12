"""
misc geometry routines

circle_area -- get area of circle
rectangle_area -- get area of rectangle

"""
from math import pi


def circle_area(diameter):
    """
    Calculate the area of a circle

    :param diameter: diameter of circle
    :return: area of circle in same units as diameter
    """
    radius = diameter / 2
    return pi * (radius ** 2)


def rectangle_area(length, width):
    """
    Calculate the area of a rectangle

    :param length: length of rectangle
    :param width: width of rectangle
    :return: area of rectangle
    """
    return length * width

if __name__ == '__main__':
    print(circle_area(22))
    print(rectangle_area(8, 9))
