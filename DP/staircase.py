import functools
functools.lru_cache()
class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        storepack={}
        def dfsstairs(n):
            if n==1 or n==2:
                return n
            elif n in storepack:
                return storepack[n]
            else:
                storepack[n]=dfsstairs(n-1) + dfsstairs(n-2)
                return storepack[n]
        return dfsstairs(A)