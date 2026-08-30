# Practical 7: Dynamic Programming - Minimum Coin Change Problem

## Objective
Solve the coin change problem using dynamic programming to find the minimum number of coins needed to make a given amount.

## Problem Statement
Given a set of coin denominations and a target amount, find the minimum number of coins required to make that amount. Also, return which coins were used.

## Concepts Covered
- **Dynamic Programming (DP)**: Breaking down complex problems into overlapping subproblems
- **Memoization**: Storing results of expensive function calls to avoid recomputation
- **Bottom-Up Approach**: Building solution from base cases upward
- **Greedy Limitation**: Why greedy approach doesn't always work (e.g., coins [1, 3, 4] with amount 6)

## Algorithm: minimum_coins()

### Approach
Uses dynamic programming with tabulation to solve the coin change problem.

**Time Complexity**: O(n × m), where n is the amount and m is the number of coin types
**Space Complexity**: O(n), where n is the amount

### How It Works

1. **Initialize Arrays**:
   - `minimum`: Stores minimum coins needed for each amount (0 to target)
   - `last_coin`: Tracks which coin was used to achieve the minimum for each amount

2. **Base Case**: 
   - minimum[0] = 0 (0 coins needed to make amount 0)

3. **Fill the DP Table**:
   - For each amount from 1 to target:
     - Try each coin denomination
     - Update if using this coin results in fewer total coins

4. **Reconstruct Solution**:
   - Backtrack using `last_coin` array to find which coins were used

### Code Structure
```python
def minimum_coins(coins, amount):
    # Initialize DP tables
    minimum = [amount + 1] * (amount + 1)
    last_coin = [-1] * (amount + 1)
    minimum[0] = 0
    
    # Fill DP table
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount and minimum[current_amount - coin] + 1 < minimum[current_amount]:
                minimum[current_amount] = minimum[current_amount - coin] + 1
                last_coin[current_amount] = coin
    
    # Check if solution exists
    if minimum[amount] == amount + 1:
        return None, []
    
    # Reconstruct the coins used
    combination = []
    current_amount = amount
    while current_amount > 0:
        coin = last_coin[current_amount]
        combination.append(coin)
        current_amount -= coin
    
    return minimum[amount], combination
```

## Example Walkthrough

### Example 1: Standard Case
**Input**: 
- Coins: [1, 2, 5]
- Amount: 11

**DP Table Evolution**:
| Amount | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|--------|---|---|---|---|---|---|---|---|---|---|----|-----|
| Coins  | - | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 2  | 3  |

**Output**: 
- Minimum coins: 3
- Coins used: [5, 5, 1] (11 = 5 + 5 + 1)

### Example 2: Impossible Case
**Input**:
- Coins: [2, 5]
- Amount: 3

**Output**: 
- Result: None (cannot make amount 3 with denominations 2 and 5)

## Key Features

### 1. Input Validation
```python
if amount < 0 or any(coin <= 0 for coin in coins):
    raise ValueError("...")
```

### 2. Solution Reconstruction
Tracks the last coin used at each amount to efficiently rebuild the solution without trying all combinations.

### 3. Impossible Amount Handling
Returns `None` if the amount cannot be formed with given coins.

## Comparison with Greedy Approach

### Greedy Approach (Fails in some cases)
```
Coins: [1, 3, 4], Amount: 6
Greedy: 4 + 1 + 1 = 3 coins (suboptimal)
```

### DP Approach (Always optimal)
```
Coins: [1, 3, 4], Amount: 6
DP: 3 + 3 = 2 coins (optimal)
```

## When to Use DP

| Characteristic | Present? |
|---|---|
| Overlapping subproblems | ✓ |
| Optimal substructure | ✓ |
| Can be solved greedily | ✗ |
| Multiple possible solutions | ✓ |

## Key Takeaways

1. **Dynamic Programming**: Essential for optimization problems where greedy fails
2. **State Representation**: Understanding what each DP state represents is crucial
3. **Reconstruction**: Storing choices (last_coin) enables backtracking to find the actual solution
4. **Verification**: Always check if a solution exists before accessing results
5. **Edge Cases**: Test with impossible amounts, single coin, and large amounts

## Practice Variations

1. Modify to find maximum coins (instead of minimum)
2. Count total number of ways to make the amount
3. Handle coin changes with weights/denominations
4. Extend to multiple currency conversions
