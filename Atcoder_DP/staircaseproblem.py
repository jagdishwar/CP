for _ in range(int(input())) :
    m=3
    n=int(input())
    flag=0
    n+=1

    def dp(m,n):
        if n<=0:
            return 1
        ans=0
        for i in range(1,m+1):
            if i<=n:
                ans= dp(m,n-i)+ans
        return ans

    print(dp(m,n))

