from algorithms.times import time_execution
from algorithms.primes import is_prime


@time_execution
def sol():

    streak = 0
    res = 0

    for a in range(-1000, 1001):
        for b in range(-1000,1001):
            prime_count = 0
            n = 0
            suspect = n**2 + a*n + b
            while suspect > 0 and is_prime(suspect):
                prime_count += 1
                n += 1
                suspect = n**2 + a*n + b
                if prime_count > streak:
                    streak = prime_count
                    res = a * b

    print(res)

sol()