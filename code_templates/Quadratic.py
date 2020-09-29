"""
A skeleton template for the Quadratic class in Week 2: Coding Exercises.
"""

import math


class Quadratic:
    """ 
    A class representing a quadratic.

    It has three variables representing a quadratic of the form 
    ax^2 + bx + c where
    a, b, and c, are real constants.

    The discriminant = b^2 - 4ac.

    If b^2 -4ac < 0 the solutions are complex and will not be calculated.
    If b^2 - 4ac = 0  then there is one real root give by -b/2a
    If b^2 - 4ac > 0  then there are two real solutions 
    """

    def __init__(self, a, b, c):
        """
        How to check have three numbers creating a quadratic. 

        Note: Not testing if one of the coefficients is zero...
        """
        if not isinstance(a, (int, float)):
            raise ValueError('Coefficient a is not a number')
        if not isinstance(b, (int, float)):
            raise ValueError('Coefficient b is not a number')
        if not isinstance(c, (int, float)):
            raise ValueError('Coefficient c is not a number')

        self.a = a
        self.b = b
        self.c = c

    def __str__( self ):
        return "Q(x) = {} x^2 + {} x + {}".format(self.a, self.b, self.c)

    def discriminant(self):
        # Replace the line below with the correct calculation of the discriminant
        disc = 1.0
        return disc

    def numberOfRoots(self):
        number = 1
        # Use flow-control to set the number of roots
        return number

    def roots(self):
        rootValues = None
        root1, root2  = None, None
        discriminant = self.discriminant()
        # calculate the roots and return them
        rootValues = (root1, root2)
        return rootValues

    @staticmethod
    def solveRoots(coefficients):
        if len(coefficients) != 3:
            print('Not a quadratic, you need three coefficients')
            return None
        for x in coefficients:
            if not isinstance(x, Number):
                print('Not a quadratic, the coefficients need to be numbers')
                return None
        q = Quadratic(coefficients[0], coefficients[1], coefficients[2])
        return q.roots()

