from functools import lru_cache
matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
m=len(matrix)
n=len(matrix[0])

def dp(i,j):
    if i>=m or j>=n:
        return 0
    if matrix[i][j]==0:
        return 0
    else:
        return min(dp(i+1,j),dp(i,j+1),dp(i+1,j+1))+1

#list1=[dp(i,j) for i in range(m) for j in range(n)]
print(dp(0,1))