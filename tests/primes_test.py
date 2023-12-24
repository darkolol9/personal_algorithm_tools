
from algorithms.primes import *


def test_is_prime():
    assert is_prime(2)


def test_get_prime_factors():
    factors, _ = get_prime_factors(13**4 * 2**5)

    assert factors == [2,13]


def test_get_nth_prime():
    assert get_nth_prime(60) == 281
