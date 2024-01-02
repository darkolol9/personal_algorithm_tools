
from math import sqrt




def eratosthenes(n):
    """
    Generates a list of prime numbers up to a given number.

    Parameters:
    - n (int): The upper limit of the range to generate prime numbers.

    Returns:
    - primes (List[int]): A list of prime numbers up to the given number.
    """
    primes = []
    composite = {}
    p = 2

    while p <= n:
        t = p * 2

        while t <= n:
            composite[t] = True
            t += p

        p += 1
        while p in composite:
            p += 1


    for i in range(2,n + 1):
        if i not in composite:
            primes.append(i)

    return primes 


def get_prime_up_to_n(n):
    """
    THIS IS THE SLOW VERSION, PLEASE REFFERE TO eratosthenes method for O(n log log n)
    Get the prime numbers up to a given number.

    Args:
        n (int): The number to get the prime numbers up to.

    Returns:
        list: A list of the prime numbers up to the given number.
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

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
    lastPrime = 2
    while count < n:
        if is_prime(num):
            count += 1
            lastPrime = num
        num += 1
        
    return lastPrime


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
            count += 1
        num += 1
  


def get_prime_factors(n: int):
    """
    Get the prime factors of a number.

    Args:
        n (int): The number to be factored.

    Returns:
        list: A list of the prime factors of the number.
    """
    powers = {}
    factors = []
    num = 2
    while num <= n:
        if n % num == 0:
            if num not in powers:
                factors.append(num)
                powers[num] = 1
            else:
                powers[num] += 1

            n //= num
        else:
            num += 1
    if n > 1:

        if num not in powers:
                factors.append(num)
                powers[num] = 1
        else:
            powers[num] += 1

    return factors, powers
