from algorithms.times import time_execution
from algorithms.primes import get_first_n_primes, is_prime
from itertools import permutations

def get_rotations_of_n(n):
    """
    Get the rotations of a number.

    Args:
        n (int): The number to be rotated.

    Returns:
        list: A list of the rotations of the number.
    """
    rotations = []
    str_n = str(n)
    for i in range(len(str_n)):
        rotations.append(int(str_n[i:] + str_n[:i]))
    return rotations


def is_circular_prime(n):
    """
    Check if a number is a circular prime.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is a circular prime, False otherwise.
    """

    perms = get_rotations_of_n(n)
    for p in perms:
        if not is_prime(p):
            return False
    return True


@time_execution
def f():

    count = 0
    primes = get_first_n_primes(1e6)

    for prime in primes:
        if prime > 1e6:
            print("last prime", prime)
            break
        
        if is_circular_prime(prime):
            count += 1
            print(prime)

    print(count)

f()
# primes = list(get_first_n_primes(1e6))

# for prime in primes:
#     print(prime)

