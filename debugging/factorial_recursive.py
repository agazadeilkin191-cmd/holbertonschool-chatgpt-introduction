#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calvulates the factorial of a non-negative integer using recursion.
    Parametrs:
    n (int): The number to calculate the factorial of.
    Returns:
    int: The factorial of the number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
      
if__name__ == " __main__ ":
    f = factorial(int(sys.argv[1]))
    print(f)
