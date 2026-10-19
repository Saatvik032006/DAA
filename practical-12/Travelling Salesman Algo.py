
INF = 99999

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
visited = [False] * n
visited[0] = True

min_cost = INF

def tsp(city, count, cost):
    global min_cost

    if count == n:
        total_cost = cost + graph[city][0]
        if total_cost < min_cost:
            min_cost = total_cost
        return

    for next_city in range(n):
        if not visited[next_city] and graph[city][next_city] != INF:
            visited[next_city] = True
            tsp(next_city, count + 1,
                cost + graph[city][next_city])
            visited[next_city] = False

tsp(0, 1, 0)

print("Minimum travelling cost:", min_cost)
