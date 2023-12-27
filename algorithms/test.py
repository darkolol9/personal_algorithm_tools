from times import time_execution
from primes import get_prime_factors, is_prime, get_nth_prime
from graphs import Graph, dfs, bfs
from _numbers import get_in_binary



@time_execution
def sol():
    print(get_in_binary(1092981))


sol()