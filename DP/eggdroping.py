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
        count=max(solve(e-1,k-1),solve(e,f-k))+1
        mn=min(mn,count)
    memo[(e,f)]=mn
    return memo[(e,f)]
e=2
f=10
value=solve(e,f)
print(value)