n=int(input())

def ETF(n):
    res=n
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            res/=i
            res*=(i-1)
            while n%i==0:
                n/=i
    if n>1:
        res/=n
        res*=(n-1)
    return res

print(ETF(n))



