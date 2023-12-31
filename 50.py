from algorithms.times import time_execution
from algorithms.primes import *




@time_execution
def f():

    limit = 1_000_000
    primes = get_prime_up_to_n(limit)
    print('finished priming', len(primes))
    prefix_sums = [2]


    for i in range(1, len(primes)):
        if prefix_sums[i - 1] + primes[i] > limit:
            break
        prefix_sums.append(prefix_sums[i - 1] + primes[i])

    print('finished prefixes', len(prefix_sums))


    max_len = 1
    top_prime = 2


    for i in range(len(prefix_sums)):
        for j in range(i):
            if is_prime(prefix_sums[i] - prefix_sums[j]):
                    if i - j > max_len:
                        max_len = i - j
                        top_prime = prefix_sums[i] - prefix_sums[j]

    print(max_len, top_prime)


f()



