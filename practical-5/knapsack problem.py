# 0/1 Knapsack Problem using Dynamic Programming

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

n = 4

# Create DP table
dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

# Dynamic Programming
for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weights[i - 1] <= w:
            include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
            exclude = dp[i - 1][w]

            if include > exclude:
                dp[i][w] = include
            else:
                dp[i][w] = exclude

        else:
            dp[i][w] = dp[i - 1][w]

# Display maximum value
print("0/1 Knapsack Problem")
print("Maximum value:", dp[n][capacity])