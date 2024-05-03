#!/usr/bin/env python

import math
import textwrap as tw


def test_function(x):
    """Function whose roots we seek."""
    return math.e**(-x) * (x*(x + 5) + 2.0) + 1.0


def bisection(fun, xrange, toll = 1e-12, niter = 1000):
    """
    A function that implements the bisection method to find the root of a
    function in a given interval.

    Parameters:
    -----------
    fun: callable
        the function to be solved
   
    xrange: list
        list containing the interval where the 0 of the function lies

    toll: float
        tolerance between two iterations, defaults to 1e-12

    niter: integer
        maximum number of iterations, defaults to 1000

    Returns:
    --------
    c: float
       root of the given equation with toll precision
  
    fc: float
       value of the given function at c (approximately 0.0)

    n: integer
       number of iterations done to reach the given solution

    """
    a = xrange[0]
    fa = fun(a)

    b = xrange[1]
    fb = fun(b)

    if fa * fb >= 0.0:
        raise ValueError("The provided function does not contain zeros in the "
                         "given interval")

    eps = 10000.0
    n = 0
    c_old = a
    fc = fa

    while eps > toll and n <= niter and fc != 0.0:

        c = (a + b) / 2
        fc = fun(c)
        if fa * fc < 0.0:
            b = c
            fb = fc
        elif fb * fc < 0.0:
            a = c
            fa = fc
        else:
            raise ValueError("Oh oh, you missed the zero")

        eps = abs(c - c_old)
        c_old = c
        n += 1

    if n == niter:
        print(f"niter, n = {n}")
        raise ValueError("Maximum number of iterations reached")

    return c, fc, n


xrange = [-1.0, 0.0]
sol, fsol, niter = bisection(test_function, xrange)

print(tw.fill(f"The root of your function is approximately x = {sol}, where "
              f"the function value is {fsol}.  This solution has been reached "
              f"after {niter} bisection iterations."))
