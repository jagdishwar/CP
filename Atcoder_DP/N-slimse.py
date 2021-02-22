from functools import lru_cache
n =int(input())

list1=list(map(int,input().split()))
acm=[0]
for i in range(n):
    acm.append(list1[i]+acm[-1])

@lru_cache(None)
def dp(i, j):
    if j-i==1:
        return 0
    cur = float('inf')
    for k in range(i + 1, j):
        cur = min(cur, acm[j] - acm[i]+dp(i, k) + dp(k, j))
    return cur


print(dp(0, n))


