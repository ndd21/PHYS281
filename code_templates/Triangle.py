"""
A skeleton template for the Triangle class in Week 2: Coding Exercises.
"""


import math


class Triangle:
    """
    A class representing a triangle.

    Parameters
    ----------
    lengthSide1: (int, float)
        The length of the first side.
    lengthSide2: (int, float)
        The length of the second side.
    lengthSide3: (int, float)
        The length of the third side.
    """

    def __init__(self, lengthSide1, lengthSide2, lengthSide3):
        self.side1 = lengthSide1
        self.side2 = lengthSide2
        self.side3 = lengthSide3

        # run test to check if triangle is valid
        if not self.testIfValidTriangle():
            raise ValueError(
                "A triangle with sides ({}, {}, {}) is not valid".format(
                     self.side1, self.side2, self.side3,    
                 )
            )

    def __str__( self ):
        return "Triangle (sides {}, {}, {})".format(self.side1, self.side2, self.side3)

    def testIfValidTriangle(self):
        test = True
        # Carry out checks that this is a triangle
        return test

    def calcTriangleArea(self):
        # Return area of the triangle 
        return area

