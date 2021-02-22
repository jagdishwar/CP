from functools import lru_cache
N = int(input())
list1= list(map(int, input().split()))


@lru_cache(None)
def dp(i):
    if i==N-1:
        return 0
    ans=dp(i+1)+abs(list1[i+1]-list1[i])

    if i+2<N:
        ans=min(ans,dp(i+2)+abs(list1[i+2]-list1[i]))

    return ans




print(dp(0))
##tabular conversation

dp=[0]*len(list1)
dp[1]=abs(list1[1]-list1[0])
for i in range(2,len(list1)):
    print(dp)
    dp[i]=min(dp[i-1]+abs(list1[i]-list1[i-1]),dp[i-2]+abs(list1[i]-list1[i-2]))
print(dp[-1])



