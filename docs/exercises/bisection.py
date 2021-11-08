#!/usr/bin/env python

import math

def test_function(x):
    return math.e**(-1 * x) * (x**2 + 5*x +2) + 1

def bisection(fun, xrange, toll = 1e-6, niter = 1000):

    """
    A function that implements the bisection method to find the root of a function in a given interval

    Parameters:
    -----------
    fun: callable
        the function to be solved
   
    xrange: list
        list containing the interval where the 0 of the function lies

    toll: float
        tolerance between two iterations, defaults to 1e-6

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

    if not (fa * fb < 0):
        raise ValueError("The provided function does not contain zeros in the given interval")

    eps = 10000
    n = 0    
    cold = a
    fc = fa

    while (eps > toll) and n <= niter and fc != 0.0:
        
        c = (a + b) / 2
        fc = fun(c) 
        if (fa * fc) < 0:
            b = c
            fb = fc
        elif (fb * fc) < 0:
            a = c
            fa = fc
        else:
            raise ValueError("Oh oh, you missed the zero")

        eps = abs(c - cold)
        cold = c
        n += 1

    if (n == niter):
       print("niter, n = ", niter, n)
       raise ValueError("Maximum number of iterations reached")
  
    return c, fc, n

xrange = [-1.0, 0.0]
sol, fsol, niter = bisection(test_function, xrange)

print("The solution of your equation is {}, where the equation is evalutaed to {}. The solution has been reached with {} iterations.".format(sol, fsol, niter))
