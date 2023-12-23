import unittest
from primes import *


class PrimesTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)


    def test_get_prime_factors(self):
        factors, _ = get_prime_factors(13**4 * 2**5)
        
        self.assertEqual(factors, [2,13])
