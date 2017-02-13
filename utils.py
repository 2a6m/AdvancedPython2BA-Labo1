# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

def fact(n):
    assert (int(n))
    assert (n >= 0)
    f = 1
    while n > 0:
        f *= n
        n -= 1
        return f


def roots(a, b, c):
    assert (int(a), int(b), int(c))
    delta = b**2 - 4*a*c
    r = (-b + delta**(1/2)) / a
    return r

def integrate(function, lower, upper):
    return 1

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))