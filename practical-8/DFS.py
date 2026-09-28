# Depth First Search (DFS) in Python
# Without using built-in functions like set(), list.remove(), etc.

# Graph represented as adjacency list
# Example:
# 0 -> 1, 2
# 1 -> 0, 3
# 2 -> 0, 4
# 3 -> 1, 4
# 4 -> 2, 3

def dfs(graph, start, visited):
    # Mark the current node as visited
    visited[start] = 1
    print(start, end=" ")

    # Visit all neighbors of the current node
    for neighbor in graph[start]:
        if visited[neighbor] == 0:
            dfs(graph, neighbor, visited)


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

print("DFS Traversal:")
dfs(graph, 0, visited)
print()

# Time Complexity:
# O(V + E) in adjacency list representation
# where V = number of vertices and E = number of edges
#
# Space Complexity:
# O(V) for the visited array and recursion stack
#
# Explanation:
# - Each vertex is visited once.
# - Each edge is checked once in the worst case.
# - For a connected graph, DFS explores every node.
