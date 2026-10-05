def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u == root_v:
        return False

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


def kruskal(vertices, edges):
    # Sort edges according to weight
    edges.sort(key=lambda x: x[2])

    parent = {}
    rank = {}

    for vertex in vertices:
        parent[vertex] = vertex
        rank[vertex] = 0

    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_weight += weight

            # MST contains V-1 edges
            if len(mst) == len(vertices) - 1:
                break

    return mst, total_weight


# Vertices
vertices = ['A', 'B', 'C', 'D', 'E', 'F']

# Edges: (source, destination, weight)
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'F', 6),
    ('E', 'F', 3)
]

# Execute Kruskal's algorithm
mst, total_weight = kruskal(vertices, edges)

# Display result
print("Edges in Minimum Spanning Tree:")

for u, v, weight in mst:
    print(u, "-", v, ":", weight)

print("Total weight of MST:", total_weight)  