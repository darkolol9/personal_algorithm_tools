

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
