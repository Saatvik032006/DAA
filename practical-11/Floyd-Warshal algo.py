INF = 99999

graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

n = len(graph)

dist = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(graph[i][j])
    dist.append(row)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

print("Shortest distance matrix:")

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print("INF", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()