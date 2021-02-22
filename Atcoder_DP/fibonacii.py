from functools import lru_cache
@lru_cache(None)
def dp(n):
    if n==0:
        return 0
    if n==1:
        return 1

    return dp(n-1)+dp(n-2)

print(dp(10))