n=90000000
sieve=[True]*n
sieve[0]=False
for i in range(2,int(n**0.5)+1):
    if sieve[i]==True:
        for j in range(i*i,n,i):
            sieve[j]=False
