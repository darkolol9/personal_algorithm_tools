from algorithms.times import time_execution
from functools import lru_cache

@lru_cache
def fib(n):
    if n < 3:
        return 1

    return fib(n - 1) + fib(n - 2)



@time_execution
def sol():
    i = 5
    while len(str(fib(i))) < 1000:
        i += 1
    print(i)


sol()