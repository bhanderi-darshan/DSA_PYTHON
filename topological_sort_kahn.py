from collections import deque, defaultdict

def topological_sort_kahn(V, adj):
    in_degree = [0] * V
    for node in adj:
        for neighbor in adj[node]:
            in_degree[neighbor] += 1

    queue = deque([v for v in range(V) if in_degree[v] == 0])
    topo_order = []

    while queue:
        vertex = queue.popleft()
        topo_order.append(vertex)
        for neighbor in adj[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == V:
        return topo_order
    else:
        return "Cycle detected – topological sort not possible"

# Example usage
if __name__ == "__main__":
    V = 6
    adj = defaultdict(list)
    adj[5].append(2)
    adj[5].append(0)
    adj[4].append(0)
    adj[4].append(1)
    adj[2].append(3)
    adj[3].append(1)

    result = topological_sort_kahn(V, adj)
    print("Topological Order (Kahn's Algorithm):", result)
