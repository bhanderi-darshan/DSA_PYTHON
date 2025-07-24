# Day 20: Dijkstra's Algorithm - Single Source Shortest Path using Min-Heap

import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))  # For undirected graph

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        min_heap = [(0, src)]

        while min_heap:
            d, u = heapq.heappop(min_heap)

            for v, weight in self.adj[u]:
                if dist[v] > d + weight:
                    dist[v] = d + weight
                    heapq.heappush(min_heap, (dist[v], v))

        print("Vertex\tDistance from Source", src)
        for i in range(self.V):
            print(f"{i}\t{dist[i]}")

# Example usage
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)

g.dijkstra(0)
