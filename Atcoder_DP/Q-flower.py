from functools import lru_cache
def dp(i,prev):
    if i>=len(nums):
        return 0
    res=dp(i+1,prev)
    if nums[i]>prev:
        res=max(val[i]+dp(i+1,nums[i]),res)
    return res
nums=[3,1,4,2]
val=[10,20,30,40]
print(dp(0,-float('inf')))

###convert into atcoder form

@lru_cache(None)
def dp(i,prev):
    if i>=len(nums):
        return 0
    res=dp(i+1,prev)
    if nums[i]>prev:
        res=max(val[i]+dp(i+1,nums[i]),res)
    return res
n=int(input())
nums=list(map(int,input().split()))
val=list(map(int,input().split()))

print(dp(0,-float('inf')))