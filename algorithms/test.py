from times import time_execution
from primes import get_prime_factors, is_prime, get_nth_prime
from graphs import Graph, dfs, bfs



@time_execution
def sol():
    a = get_nth_prime(60)
    print(is_prime(a))
    


sol()