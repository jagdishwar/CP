memo={}
def solve(e,f):
    if f==0 or f==1:
        return f
    if e==1:
        return f
    if (e,f) in memo:
        return memo[(e,f)]

    mn=float('inf')
    for k in range(1,f+1):
        if (e-1,k-1) in memo:
            low=memo[(e-1,k-1)]
        else:
            low=solve(e-1,k-1)
            memo[(e-1,k-1)]=low
        if (e,f-k) in memo:
            high=memo[(e,f-k)]
        else:
            high=solve(e,f-k)
            memo[(e,f-k)]=high
        count=1+max(high,low)
        mn=min(mn,count)

    memo[(e,f)]=mn
    return memo[(e,f)]
e=2
f=10
value=solve(e,f)
print(value)