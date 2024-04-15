from algorithms._numbers import *

def test_gcd():
    assert gcd(15, 10) == 5
    assert gcd(10, 15) == 5
    assert gcd(15, 15) == 15

def test_get_proper_divisors():
    assert get_proper_divisors(15) == [1, 3, 5]

