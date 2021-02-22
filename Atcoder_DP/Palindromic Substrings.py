from functools import lru_cache
class Solution:
    def countSubstrings(self, s: str) -> int:
            strx=s
            list1=[0]
            set1=set()
            @lru_cache(None)
            def dp(i,j):
                if i<=j and (i,j) not in set1:
                    if i>=len(strx) or j>=len(strx):
                        return 0
                    if strx[i:j+1]==strx[i:j+1][::-1]:
                        list1[0]+=1
                    set1.add((i,j))
                    dp(i,j+1)
                    dp(i+1,j)

            dp(0,0)
            return (list1[0])
