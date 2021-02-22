from functools import lru_cache
weights=[3,4,5]
val=[30,50,60]
#mininum weights to gets that value
@lru_cache(None)
def dp(index,capacity):
    if index>=len(weights) :
        if capacity<=0:
            return 0
        else:
            return float('inf')
    if val[index]>capacity:
        return dp(index+1,capacity)
    else:
        return min(weights[index]+dp(index+1,capacity-val[index]),dp(index+1,capacity))

capacity=8
maxvalue=-float('inf')
for i in range(sum(val),-1,-1):
    if dp(0,i)<=capacity:
        maxvalue=max(i,maxvalue)
print(maxvalue)

#conversation into tabular
a,capacity=map(int,input().split())
weights=[0]
val=[0]
for i in range(a):
    w,v =map(int,input().split())
    weights.append(w)
    val.append(v)


dp=[[float('inf') for i in range(sum(val)+1)] for j in range(a+1)]

for i in range(a+1):
    for j in range(sum(val)+1):
        if j==0:
            dp[i][j]=0
        elif val[i]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=min(weights[i]+dp[i-1][j-val[i]],dp[i-1][j])

maxvalue=-float('inf')
for i in range(sum(val),-1,-1):
    if dp[-1][i]<=capacity:
        maxvalue=max(maxvalue,i)


print(maxvalue)


