from times import time_execution
from primes import get_prime_factors, is_prime
from graphs import Graph, dfs, bfs
















@time_execution
def sol():
    a, b = get_prime_factors(13**4 * 2**5)
    print(a,b)
    


sol()