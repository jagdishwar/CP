list1=[2,3,5,8,10]
sum1=10
t=[]
for i in range(len(list1)+1):
    list2=[]
    for j in range(sum1+1):
        list2.append(0)
    t.append(list2)

for i in range(len(list1)+1):
    t[i][0]=1

print(t)
for i in range(1,len(list1)+1):
    for j in range(1,sum1+1):
        if list1[i-1]<=j:
            t[i][j]=t[i-1][j-list1[i-1]] + t[i-1][j]
        elif list1[i-1]>j:
            t[i][j]=t[i-1][j]

print(t[-1][-1])
list1=[2,3,5,8,10]
sum1=10
memo={}
def subsetsumcount(list1,sum1,n):
    if n==0 and sum1!=0:
        return 0
    if n!=0 and sum1==0:
        return 1
    if n==0 and sum1==0:
        return 1
    if (n,sum1) in memo:
        return memo[(n,sum1)]
    if list1[n-1]<=sum1:
        memo[(n,sum1)]=subsetsumcount(list1,sum1-list1[n-1],n-1) + subsetsumcount(list1,sum1,n-1)
        return memo[(n,sum1)]
    elif list1[n-1]>sum1:
        memo[(n,sum1)]=subsetsumcount(list1,sum1,n-1)
        return memo[(n,sum1)]
n=len(list1)
value=subsetsumcount(list1,sum1,n)
print(value)
