
# Day 25: Floyd-Warshall Algorithm for All-Pairs Shortest Paths

INF = float('inf')

def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [row[:] for row in graph]  # Create a copy of the graph matrix

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example graph represented as an adjacency matrix
graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

shortest_paths = floyd_warshall(graph)

print("All-Pairs Shortest Paths (Floyd-Warshall):")
for row in shortest_paths:
    print(row)
