
# Day 24: Prim's Algorithm - Minimum Spanning Tree (MST)
# Using Priority Queue (Min Heap)

import heapq

def prim_mst(graph, start_node):
    mst = []
    visited = set()
    min_heap = [(0, start_node, -1)]  # (weight, current_node, parent_node)

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)
        if current not in visited:
            visited.add(current)
            if parent != -1:
                mst.append((parent, current, weight))

            for neighbor, edge_weight in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst

# Example graph as adjacency list
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

start_node = 0
mst_result = prim_mst(graph, start_node)
print("Minimum Spanning Tree using Prim's Algorithm:")
for u, v, w in mst_result:
    print(f"{u} - {v} with weight {w}")
