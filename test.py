from times import time_execution
from primes import get_prime_factors, is_prime
from graphs import Graph, dfs, bfs















@time_execution
def build():
    graph = Graph(5000)
    graph.randomize_edges(0.01)
    return graph

@time_execution
def sol(g):
    distances, colors = bfs(g, 0)
    print(g.edges)





g = build()
sol(g)