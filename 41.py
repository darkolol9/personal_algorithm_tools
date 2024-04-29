from algorithms.primes import eratosthenes, is_prime
from algorithms.times import time_execution
from itertools import permutations



n = 7
@time_execution
def sol():
    nine_digits = list(permutations(list(range(1,n + 1)), n))

    for seq in nine_digits[::-1]:
        num = int(''.join([str(i) for i in seq]))

        if is_prime(num):
            print(num)
            break





sol()
