# Prim's Algorithm

# Weighted graph represented using an adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

vertices = len(graph)

# To keep track of vertices included in MST
selected = [False] * vertices

# Start from vertex 0
selected[0] = True

print("Edges in the Minimum Spanning Tree:")

edges = 0

while edges < vertices - 1:
    minimum = float('inf')
    x = 0
    y = 0

    for i in range(vertices):
        if selected[i]:
            for j in range(vertices):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(f"Vertex {x} - Vertex {y} : Weight {graph[x][y]}")

    selected[y] = True
    edges += 1
