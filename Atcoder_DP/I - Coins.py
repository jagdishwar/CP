from functools import lru_cache
n=int(input())
list1=list(map(float,input().split()))
@lru_cache(None)
def dp(i,head,n):
    if i==n:
        if head>(n//2):
            return 1
        else:
            return 0
    m=dp(i+1,head+1,n)*list1[i]
    n=dp(i+1,head,n)*(1-list1[i])

    return m+n

print(dp(0,0,n))
### with the better time complexity

import sys

sys.setrecursionlimit(10 ** 7)
n = int(input())
list1 = list(map(float, input().split()))
it = [[-1 for i in range(n + 1)] for j in range(n + 1)]


def dp(i, head, n):
    if i == n or n - head == (n // 2):
        if head > (n // 2):
            return 1
        else:
            return 0
    if it[i][head] != -1:
        return it[i][head]

    it[i][head] = list1[i] * dp(i + 1, head + 1, n) + dp(i + 1, head, n) * (1 - list1[i])
    return it[i][head]


print(dp(0, 0, n))




