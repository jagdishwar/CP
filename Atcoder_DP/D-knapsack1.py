from functools import lru_cache
weights=[0]
val=[0]
@lru_cache(None)
def dp(index,capacity):
    if capacity<=0 or index>=len(weights):
        return 0

    if weights[index]>capacity:
        return dp(index+1,capacity)
    else:
        return max(dp(index+1,capacity),val[index]+dp(index+1,capacity-weights[index]))

a,capacity=map(int,input().split())


for i in range(a):
    w,v=map(int,input().split())
    weights.append(w)
    val.append(v)


print(dp(0,capacity))

#conversion into bottom up

dp = [[0 for i in range(capacity + 1)] for j in range(a + 1)]

for i in range(a + 1):
    for j in range(capacity + 1):
        if weights[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(val[i] + dp[i - 1][j - weights[i]], dp[i - 1][j])

print(dp[-1][-1])