# Practical 4: Recursion and Factorial Calculation

## Objective
Understand recursion and iterative approaches by implementing factorial calculation using both methods.

## Concepts Covered
- **Recursion**: A function calling itself with a smaller input until reaching a base case
- **Iteration**: Using loops to solve problems without function recursion
- **Base Case**: The condition that stops the recursion
- **Stack Overflow**: Risk when recursion depth exceeds system limits

## Files

### 1. factorial.py - Iterative Approach
**Description**: Calculates factorial using an iterative approach (loops)

**Algorithm**:
- Multiply all integers from 1 to n
- Time Complexity: O(n)
- Space Complexity: O(1)

**Code Structure**:
```python
def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result
```

**Advantages**:
- No risk of stack overflow
- Generally faster execution
- Easier to understand for beginners

### 2. recursive.py - Recursive Approach
**Description**: Calculates factorial using recursion (function calling itself)

**Algorithm**:
- Base Case: factorial(0) = 1, factorial(1) = 1
- Recursive Case: factorial(n) = n × factorial(n-1)
- Time Complexity: O(n)
- Space Complexity: O(n) - due to call stack

**Code Structure**:
```python
def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)
```

**Advantages**:
- More elegant and concise code
- Directly mirrors mathematical definition
- Easier to understand the problem structure

**Disadvantages**:
- Risk of stack overflow for large n
- Function call overhead makes it slightly slower

## Comparison

| Aspect | Iterative | Recursive |
|--------|-----------|-----------|
| Stack Overflow Risk | No | Yes (for large n) |
| Space Complexity | O(1) | O(n) |
| Time Complexity | O(n) | O(n) |
| Code Readability | Clear | Elegant |
| Execution Speed | Faster | Slower |

## Example Usage

**Input**: 5

**Iterative Output**: 
```
Factorial of 5 is 120
(5 × 4 × 3 × 2 × 1 = 120)
```

**Recursive Output**: Same result, different execution path
```
5 × factorial(4)
5 × 4 × factorial(3)
5 × 4 × 3 × factorial(2)
5 × 4 × 3 × 2 × factorial(1)
5 × 4 × 3 × 2 × 1 = 120
```

## Key Takeaways
1. Both approaches solve the same problem with different methodologies
2. Iterative is preferred for factorial due to efficiency
3. Recursion is powerful for tree/graph problems and problems with recursive structure
4. Always consider stack limitations when using recursion
5. Test edge cases: negative numbers, 0, 1, large numbers
