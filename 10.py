from algorithms.times import time_execution
from algorithms.primes import *




@time_execution
def solve():
    print(sum(get_prime_up_to_n(int(2e6))))

solve()