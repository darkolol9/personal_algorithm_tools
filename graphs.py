from random import random


class Graph:
    def __init__(self, vertices):
        """
        Initializes a new instance of a graph

        Parameters:
            vertices (int): The number of vertices in the graph.

        Returns:
            None
        """
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        
        self.edges = 0

    def add_edge(self, v1, v2):
        self.graph[v1][v2] = 1
        self.graph[v2][v1] = 1
        self.edges += 1

    def remove_edge(self, v1, v2):
        self.graph[v1][v2] = 0
        self.graph[v2][v1] = 0
        self.edges -= 1

    def is_edge(self, v1, v2):
        return self.graph[v1][v2] or self.graph[v2][v1]
    
    def neighbors(self, v):
        return [i for i, x in enumerate(self.graph[v]) if x == 1]
    

    def randomize_edges(self, chance = 0.5):
        for i in range(self.vertices):
            for j in range(i):
                if (random() < chance and not self.is_edge(i, j)):
                    self.add_edge(i, j)

    
    


def dfs_visit(graph: Graph, start: int, colors, distances):
    """
    Perform a depth-first search (DFS) visit on a graph, starting from a given node.

    Args:
        graph (Graph): The graph to perform the DFS visit on.
        start (int): The starting node for the DFS visit.
        colors (list): A list representing the colors of each node in the graph.
        distances (list): A list representing the distances of each node from the starting node.

    Returns:
        None
    """
    colors[start] = "gray"
    for u in graph.neighbors(start):
        if colors[u] == "white":
            distances[u] = distances[start] + 1
            dfs_visit(graph, u, colors, distances)
    colors[start] = "black"



def dfs(graph: Graph, start_vertex:int):
    """
    Depth-first search on a graph starting from a given vertex.

    Parameters:
        graph (Graph): The graph to perform the depth-first search on.
        start_vertex (int): The starting vertex for the depth-first search.

    Returns:
        dict: A dictionary mapping each vertex to its distance from the starting vertex.
        and a colors map, representing if nodes have been visited or not
    """
    colors = {v: "white" for v in range(graph.vertices)}
    distances = {v : None for v in range(graph.vertices)}

    distances[start_vertex] = 0
    colors[start_vertex] = "gray"

    for u in graph.neighbors(start_vertex):
        if colors[u] == "white":
            distances[u] = distances[start_vertex] + 1
            dfs_visit(graph, u, colors, distances)

    colors[start_vertex] = "black"
    return distances, colors



# example run
if __name__    == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 2)
    graph.add_edge(0, 4)


    print(dfs(graph, 2))