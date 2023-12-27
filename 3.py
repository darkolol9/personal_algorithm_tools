from algorithms.times import time_execution
from algorithms.primes import get_prime_factors, is_prime






@time_execution
def f():
    print(get_prime_factors(600851475143))

f()

