# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

def fact(n):
    # Python program to find the factorial of a number provided by the user.

    # change the value for a different result

    # uncomment to take input from the user
    # num = int(input("Enter a number: "))

    factorial = 1

    # check if the number is negative, positive or zero
    if n < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        print("The factorial of", n, "is", factorial)


def roots(a, b, c):
    assert (int(a), int(b), int(c))
    delta = b**2 - 4*a*c
    if a == 0:
        r = (-b + delta**(1/2))
        return r
    r = (-b + delta**(1/2) / a)
    return r

def integrate(function, lower, upper):
    return 1

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))