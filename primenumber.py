from math import sqrt

def squareroot(p,k):
    for i in range(2,k+2):
        if p%i==0 :
            return False

list1=[2]

for i in range(2,A):
        p=int(i)
        k=int(p//2)
        ret=squareroot(p,k)
        if ret == False:
            pass
        else:
            list1.append(p)

print(list1)

for i in range(len(list1)):
    for j in range(i,len(list1)):
        ko=list1[i]+list1[j]
        if ko==A:
            print(list1[i],list1[j])

print(int(6,2))