# Implementation of chain matrix multiplication using dynamic programming.

def matrix_chain_order(p):
    n = len(p) - 1

    # m[i][j] = minimum number of scalar multiplications
    # needed to multiply matrices Ai...Aj
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    # s[i][j] stores the position at which the optimal split occurs
    s = [[0] * (n + 1) for _ in range(n + 1)]
    

    # L is the chain length
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    return m, s


def print_optimal_parenthesis(s, i, j):
    if i == j:
        return f"A{i}"

    k = s[i][j]

    left = print_optimal_parenthesis(s, i, k)
    right = print_optimal_parenthesis(s, k + 1, j)

    return f"({left} × {right})"


# Input: dimensions of matrices
# A1 = 10x30, A2 = 30x5, A3 = 5x60
p = [10, 30, 5, 60]

m, s = matrix_chain_order(p)

n = len(p) - 1

print("Minimum number of scalar multiplications:", m[1][n])
print("Optimal parenthesization:", print_optimal_parenthesis(s, 1, n))