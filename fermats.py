# a.a^-1=1 (mod m)- a/a==1
## fermat's theorem
## a^m-1==1(mod m)
## a^m-2=a^-1(mod m) ------(m supposed to be a prime and (m,a) must be coprime)
def power(x,n,mod):
    ans=1
    while n:
        if int(n)&1:
            ans= (ans*x)%mod
            n-=1
        else:
            x=(x*x)%mod
            n//=2
    return ans

def modular_inverse(a,m):
    return power(a,m-2,m)


print(modular_inverse(3,11))
