# Practical 12: Travelling Salesman Problem

## Summary

This Python program solves the Travelling Salesman Problem (TSP) by finding the minimum cost route that starts and ends at the same city while visiting every city exactly once. It uses backtracking to explore all possible paths and keeps track of the least total cost.

The program is a classic example of exhaustive search in graph optimization. Although it is not the most efficient approach for large graphs, it is useful for understanding how brute-force algorithms work.

## Problem Solved

Given a complete weighted graph, the program determines the shortest possible tour that visits all cities and returns to the starting city. In this example, city 0 is the starting point.

## Algorithm Explanation

1. Mark the starting city as visited.
2. Recurse through all remaining unvisited cities.
3. Add the cost of each selected edge to the current route cost.
4. When all cities have been visited, return to the starting city and compare the total route cost with the minimum cost found so far.
5. Backtrack to explore other possible routes.

## Time Complexity

- Time Complexity: O(n!)
- Space Complexity: O(n)

Where `n` is the number of cities in the graph.

This happens because the algorithm checks all possible permutations of the cities in the worst case.

## Example Used in the Program

The graph is represented by the following cost matrix:

- 0 to 1 = 10
- 0 to 2 = 15
- 0 to 3 = 20
- 1 to 2 = 35
- 1 to 3 = 25
- 2 to 3 = 30

The program computes the minimum cycle cost by checking different city orders.

## Output

When the program runs, it prints:

```text
Minimum travelling cost: 80
```

This means the minimum route cost is 80.

## Conclusion

The Travelling Salesman Problem is an important optimization problem in algorithm design. This practical demonstrates how recursion and backtracking can be used to search all possible tours and select the best one. Although the brute-force method is suitable for small inputs, larger instances require more advanced optimization techniques such as dynamic programming or approximation methods.
