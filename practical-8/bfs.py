# Breadth First Search (BFS) in Python
# Without using built-in functions like set(), deque(), etc.

# Graph represented as adjacency list
# Example:
# 0 -> 1, 2
# 1 -> 0, 3
# 2 -> 0, 4
# 3 -> 1, 4
# 4 -> 2, 3


def bfs(graph, start, visited):
    queue = [start]
    visited[start] = 1

    while len(queue) > 0:
        vertex = queue[0]
        print(vertex, end=" ")
        queue = queue[1:]

        for neighbor in graph[vertex]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                queue.append(neighbor)


# Driver code
vertices = 5
visited = [0] * vertices

# Adjacency list
graph = [
    [1, 2],
    [0, 3],
    [0, 4],
    [1, 4],
    [2, 3]
]

print("BFS Traversal:")
bfs(graph, 0, visited)
print()

# Time Complexity:
# O(V + E) in adjacency list representation
# where V = number of vertices and E = number of edges
#
# Space Complexity:
# O(V) for the visited array and queue
#
# Explanation:
# - Each vertex is visited once.
# - Each edge is checked at most once.
# - BFS explores nodes level by level.
