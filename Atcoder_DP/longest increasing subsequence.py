from functools import lru_cache

nums=[0,1,0,3,2,3]

n=len(nums)
@lru_cache(None)
def dp(i,prev):
    if i>=len(nums):
        return 0
    res=dp(i+1,prev)
    if nums[i]>prev:
        res=max(1+dp(i+1,nums[i]),res)
    return res

print(dp(0,-float('inf')))

dp=[1]*n
for j in range(n):
    for i in range(j):
        if nums[i]<nums[j]:
            dp[j]=max(dp[j],1+dp[i])

print(dp[i])
key=i



it=[1]*n
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if nums[i]>nums[j]:
            it[i]=max(it[i],it[j]+1)
print(it)
print(it[i])


