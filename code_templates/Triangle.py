"""
A skeleton template for the Triangle class in Week 2: Coding Exercises.
"""


import math


class Triangle:
    """
    A class representing a triangle
    """

    def __init__(self, lengthSide1, lengthSide2, lengthSide3):
        self.side1 = lengthSide1
        self.side2 = lengthSide2
        self.side3 = lengthSide3

    def __str__( self ):
        return "Triangle (sides {}, {}, {})".format(self.side1, self.side2, self.side3)

    def testIfValidTriangle(self):
        # Use static method so can use without creating object as well and
        # only have one defnition.
        return Triangle.testIfTriangle(self.side1, self.side2, self.side3)

    def calcTriangleArea(self):
        area = float('nan')  # If not a valid triangle the area has no meaning...
        # Return area if valid triangle 
        return area

    @classmethod 
    def triangleFromList(cls, sides):
        if len(sides) != 3:
            raise ValueError('Not a triangle, you needs three sides ')

        for length in sides:
            if not isinstance(length, (int, float)):
                raise ValueError('Not a triangle, you need three numbers')

        return cls(sides[0], sides[1], sides[2])

    @staticmethod
    def testIfTriangle(lengthSide1, lengthSide2, lengthSide3):
        test = True
        # Carry out checks that this is a triangle
        return test

