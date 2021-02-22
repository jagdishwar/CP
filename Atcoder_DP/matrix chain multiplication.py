import numpy as np

def dp(i, j):
    if j-i <= 2:
        return 0
    minimum = float('inf')
    for k in range(i+1, j-1):
        minimum = min(dims[i]*dims[j-1]*dims[k]+dp( i,k+1) +dp( k, j)
                    ,minimum)
    return minimum


dims=[3, 3, 2, 1, 2]

print(dp(0,len(dims)))

#with memoization

def dp(i, j):
    if j-i <= 2:
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    minimum = np.inf
    for k in range(i+1, j-1):
        minimum = min(dims[i]*dims[j-1]*dims[k]+dp( i, k+1) + dp( k, j)
                    ,minimum)
    memo[(i,j)] = minimum
    return minimum

memo = {}
dims=[3, 3, 2, 1, 2]

print(dp(0,len(dims)))