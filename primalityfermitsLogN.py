import random
def power(x,n,mod):
    ans=1
    while n:
        if int(n)&1:
            ans=(ans%mod*x%mod)%mod
        x=(x%mod*x%mod)%mod
        n//=2
    return ans


def primality(n):
    if n<5:
        return n==2 or n==3
    for _ in range(5):
        a=random.randint(2,n-2)
        if power(a,n-1,n)!=1:
            return False
    return True
for _ in range(int(input())):
        if primality(int(input())):
            print('YES')
        else:
            print('NO')

