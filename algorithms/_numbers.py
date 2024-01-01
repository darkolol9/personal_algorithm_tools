from functools import cache


    
import math

def num_of_divisors(n):
    """
    Get the number of divisors of a number.

    Args:
        n (int): The number to be factored.

    Returns:
        int: The number of divisors of the number.
    """
    count = 2  # accounts for 'n' and '1'
    
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            if i == (n // i):
                # if the divisors are the same, count only once
                count += 1
            else:
                # else, count both
                count += 2

    return count



def get_divisors(n):
    """
    Get the divisors of a number.

    Args:
        n (int): The number to be factored.

    Returns:
        list: A list of the divisors of the number.
    """
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors + [n]

def get_proper_divisors(n):
    """
    Get the proper divisors of a number.

    Args:
        n (int): The number to be factored.

    Returns:
        list: A list of the proper divisors of the number.
    """
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def gcd(a, b):
    """
    Calculates the greatest common divisor (GCD) of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of the two numbers.
    """

    if b == 0:
        return a
    
    return gcd(b, a % b)


def get_in_binary(n):
    """
    Get the binary representation of a number.

    Args:
        n (int): The number to be converted.

    Returns:
        str: The binary representation of the number.
    """
    return bin(n)[2:]
