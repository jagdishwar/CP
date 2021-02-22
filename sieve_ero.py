n=20
prime=[True]*n
for i in range(2,int(n/2)):
    if prime[i]==True:
        for j in range(i*2,n,i):
            prime[j]=False

print(prime)
list1=[]
for i in range(2,len(prime)):
    if prime[i]==True:
        list1.append(i)

print(list1)
