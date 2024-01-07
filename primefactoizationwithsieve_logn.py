n=50
sieve=[True]*(n+1)
sieve[0]=False

for i in range(2,int(n**0.5)+1):
    if sieve[i]==True:
        for j in range(i,n+1,i):
            if sieve[j]==True:
                sieve[j]=i
print(sieve[50])
