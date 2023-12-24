from algorithms._numbers import get_proper_divisors
from algorithms.primes import get_nth_prime, is_prime
from algorithms.times import time_execution
from algorithms.graphs import *



@time_execution
def sol():
    abundents = []


    seen = {}
    for i in range(1, 28_123):
        if sum(get_proper_divisors(i)) > i:
            abundents.append(i)

            
    total = sum([i for i in range(1, 28123)])


    for i in range(len(abundents)):
        for j in range(len(abundents)):
            num = abundents[i] + abundents[j]
            if (num < 28_123 and num not in seen):
                seen[num] = True
                total -= (num)


    return total

print(sol())
