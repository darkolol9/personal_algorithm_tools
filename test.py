from times import time_execution
from primes import get_prime_factors, is_prime
from graphs import Graph, dfs














@time_execution
def sol():
    graph = Graph(5)
    graph.randomize_edges(2)

    distances, colors = dfs(graph, 0)
    print(distances, graph.edges)





sol()