# Practical 11: Floyd-Warshall Algorithm

## Summary

This Python program implements the Floyd-Warshall algorithm to find the shortest path between all pairs of vertices in a weighted graph. It is a classic dynamic programming approach used for solving the all-pairs shortest path problem.

The algorithm works by considering every vertex as a possible intermediate node and updating the shortest known distance between each pair of vertices. This helps in finding the minimum cost path between any two nodes in the graph.

## Problem Solved

Given a weighted graph, the program computes the shortest path distances between every pair of vertices. It handles graphs with no direct connection by using a large value, `INF`, to represent infinity.

## Algorithm Explanation

1. Initialize a distance matrix with the graph's direct edge values.
2. Set `INF` for unreachable paths.
3. For each vertex `k`, check whether a path from `i` to `j` can be improved by going through `k`.
4. Update the distance if:
   `dist[i][j] > dist[i][k] + dist[k][j]`
5. Repeat until all vertices have been considered as intermediate nodes.

## Time Complexity

- Time Complexity: O(V³)
- Space Complexity: O(V²)

Where `V` is the number of vertices in the graph.

## Example Used in the Program

The graph in the code is:

- 0 to 1 = 5
- 1 to 2 = 3
- 2 to 3 = 1
- 0 to 3 = 10

The final shortest distance matrix produced by the program is:

```text
0  5  8  9
INF  0  3  4
INF  INF  0  1
INF  INF  INF  0
```

This output shows the shortest distances between all pairs of vertices.

## Output

When the program runs, it prints:

```text
Shortest distance matrix:
0 5 8 9
INF 0 3 4
INF INF 0 1
INF INF INF 0
```

## Conclusion

The Floyd-Warshall algorithm successfully computes the shortest distances between all pairs of vertices in a weighted graph. It is especially useful when the graph is dense and we need all shortest paths rather than only the shortest path between one source and one destination. This practical demonstrates the power of dynamic programming in solving graph optimization problems efficiently.
