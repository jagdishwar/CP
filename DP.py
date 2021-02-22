N = 5
tax =[1,6,5,7]
K = 1




dp = [float('inf')]*(N+K)
dp[0] = 0
for i in range(1, N):
    dp[i:i + K] = min(dp[i:i + K],int(tax[i-1]) + dp[i - 1])
print(dp[-1])
"""
dp = [0] * N
for i in range(1, N):
    min_cost = INF
    for k in range(1, min(K + 1, i + 1)):
        cost = dp[i - k] + abs(h[i] - h[i - k])
        if cost < min_cost:
            min_cost = cost
    dp[i] = min_cost
print(dp[-1])
"""