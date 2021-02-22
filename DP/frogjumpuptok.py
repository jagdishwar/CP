tax = [1,6,-1,2,3,7]
N=len(tax)
K=2

dp = [float('inf')] * N
dp[0] = 0

for i in range(N):
    for k in range(i + 1, min(i + K + 1, N)):
            if tax[i]==-1:
                dp[k]=dp[k-1]
            else:
                dp[k] = min(dp[k], dp[i] +tax[i])

print(dp[-1])

"""def dfsdeploy(ind):
    if ind==n:
        return 0
    minvalue=float('inf')
    for i in range(ind+1,min(n,k+ind)+1):
        minvalue=(min(abs(arr[i]-arr[ind]),minvalue))+dfsdeploy(i)

    return minvalue


print(dfsdeploy(0))"""