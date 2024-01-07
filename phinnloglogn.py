n=1000000
phi=[0]*(n+1)
def phisieve(n):
    for i in range(1,n+1):
        phi[i]=i
    for i in range(2,n+1):
        if phi[i]==i:
            for j in range(i,n+1,i):
                phi[j]/=i
                phi[j]*=i-1

phisieve(n)

print(phi[81])






