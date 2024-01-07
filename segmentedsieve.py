n=100001
sieve=[True]*n
sieve[0]=False
sieve[1]=False
def sievefuc():
    for i in range(2,int(n**0.5)+1):
        if sieve[i]==True:
            for j in range(i*i,n,i):
                sieve[j]=False
sievefuc()
for _ in range(int(input())):
    L,R=map(int,input().split())
    if L==1:
        L+=1
    n = R - L + 1
    segsieve = [True] * (n + 1)
    def segmentedsieve(L,R):
        for k,v in enumerate(sieve):

            if k>R**0.5:
                break
            elif v==True:

                i=int(L//k)*k
                if i<L:
                    i+=k
                for j in range(i,R+1,k):
                    if j!=k:
                        segsieve[L-j]=False

    segmentedsieve(L,R)

    for i in range(L,R+1):
        if segsieve[L-i]:
            print(i)













