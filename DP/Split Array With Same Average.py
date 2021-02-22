#~A=~B
--- ----
# a  b

#
#
#
#
#
A=[1,7,15,29,11,9]
N=len(A)
sum1=sum(A)
ispossible=[]
for j in range(1,N//2+1):
    if (sum1*j)%N==0:
        ispossible.append(j)

sett=[set() for _ in range((N//2)+1)]
sett[0].add(0)
for n in A:
    for i in range(N//2,0,-1):
        for k in sett[i-1]:
            sett[i].add(n+k)
print(sett)
for i in ispossible:
    if (sum1*i)/N in sett[i]:
        print((sum1*i)/N)
        print((sum1))
        print('True')
print('False')