def phiphi(x):
    n=100000
    phi=[1]*(n+1)
    for i in range(2,n+1):
        phi[i]=i
    for i in range(2,n+1):
        if phi[i]==i:
            for j in range(i,n+1,i):
                phi[j]/=i
                phi[j]*=(i-1)
    return phi[int(x)]

def countgcd(num,gcd):

    return phiphi(num/gcd)


ans=0
num=int(input())
for i in range(1,int(num**0.5)+1):
    if num%i==0:
        d1=i
        d2=num/i
        c1=countgcd(num,d1)
        c2=countgcd(num,d2)
        ans+=d1*c1
        ans+=d2*c2


print(ans)




