from algorithms.primes import eratosthenes
from algorithms.times import time_execution



@time_execution
def f():
    print(eratosthenes(2000_000)[10_000])

f()