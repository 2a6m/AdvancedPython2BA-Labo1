# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

import math as m

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    return m.factorial(n)

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    assert (int(a))
    assert (int(b))
    assert (int(c))
    delta = b ** 2 - 4 * a * c
    if a == 0:
        rp = (-b + m.sqrt(delta))
        rn = (-b - m.sqrt(delta))
        return rp, rn
    rp = (-b + m.sqrt(delta) / a)
    rn = (-b - m.sqrt(delta) / a)
    return rp, rn

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    return 1

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))

