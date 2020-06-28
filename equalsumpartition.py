list1=[10,2,3,5,2,2]
sum1=6
t=[]
for i in range(len(list1)+1):
    list2=[]
    for j in range(sum1+1):
        list2.append(0)
    t.append(list2)
print(t)
for l in range(len(list1)+1):
    for m in range(1,sum1+1):
        t[l][0]=True
        t[0][m]=False
print(t)

for i in range(1,len(list1)+1):
    for j in range(1,sum1+1):
        if list1[i-1]<=j:
            t[i][j]=t[i-1][j-list1[i-1]] or t[i-1][j]
        elif list1[i-1]>j:
            t[i][j]=t[i-1][j]

print(t[-1][-1])
n=len(list1)
list1=[10,2,3,5,2,2]
sum1=6
memo={}
def subset(list1,sum1,n):
    if sum1==0 and n!=0:
        return True
    if sum1!=0 and n==0:
        return False
    if sum1==0 and n==0:
        return True
    if (n,sum1) in memo:
        return memo[(n,sum1)]
    if list1[n-1]<=sum1:
        memo[(n,sum1)] =subset(list1,sum1-list1[n-1],n-1) or subset(list1,sum1,n-1)
        return memo[(n,sum1)]
    elif list1[n-1]>sum1:
        memo[(n,sum1)]=subset(list1,sum1,n-1)
        return memo[(n,sum1)]

val=subset(list1,sum1,n)
print(val)
list1=[11,5,2,5]
n=len(list1)
if sum(list1)%2==0:
       end=subset(list1,sum1//2,n)
       print(end)
else:
    print('go back to your home ,cold war is going on')



