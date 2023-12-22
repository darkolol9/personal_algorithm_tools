

from math import sqrt

def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_nth_prime(n):
    """
    Get the nth prime number.

    Args:
        n (int): The index of the prime number to be returned.

    Returns:
        int: The nth prime number.
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num


def get_first_n_primes(n: int):
    """
    Get the first n prime numbers.

    Args:
        n (int): The number of prime numbers to be returned.

    Returns:
        list: A list of the first n prime numbers.
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
        num += 1
  


def get_prime_factors(n: int):
    """
    Get the prime factors of a number.

    Args:
        n (int): The number to be factored.

    Returns:
        list: A list of the prime factors of the number.
    """
    factors = []
    num = 2
    while num * num <= n:
        if n % num == 0:
            yield num
            n //= num
        else:
            num += 1
    if n > 1:
        yield n
    return factors
