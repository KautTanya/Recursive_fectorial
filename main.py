"""Recursive_factorial"""


def recursive_factorial(n):
    """Recursive_factorial"""
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


print(recursive_factorial(5))
