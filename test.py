from times import time_execution
from primes import get_prime_factors, is_prime
from graphs import Graph, dfs














@time_execution
def sol():
    g1 = Graph(100)
    g1.randomize_edges(0.01)

    print(dfs(g1, 0), g1.edges)


    # print(list(get_prime_factors(133939153441)))





sol()