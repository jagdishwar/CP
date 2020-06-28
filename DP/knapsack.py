memo={}
def knapsack(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if (n,W) in memo:
        return memo[(n,W)]
    elif wt[n-1]<=W:
        memo[(n,W)]=(max((val[n-1]+knapsack(wt,val,W-wt[n-1],n-1)),knapsack(wt,val,W,n-1)))
        return memo[(n,W)]
    elif wt[n-1]>W:
        memo[(n,W)]=knapsack(wt,val,W,n-1)
        return memo[(n,W)]
wt=[4,3,2,5,6,7,2,5,5]
n=len(wt)
val=[1,2,3,4,5,6,7,8,9]
W=9
output=knapsack(wt,val,W,n)
print(output)

t=[]
for i  in range(0,len(wt)+1):
    list1=[]
    for j in range(0,W+1):
        list1.append(0)
    t.append(list1)
for i in range(1,len(wt)+1):
    for j in range(1,W+1):
        if wt[i-1]<=j:
            t[i][j]=max((val[i-1]+t[i][j-wt[i-1]]),t[i-1][j])
        elif wt[i-1]>j:
            t[i][j]=t[i-1][j]
print(t[-1][-1])
print(t)
####printing result
i=len(wt)
j=W
result=[]
while i>0 and j>0:
    if max(t[i-1][j],t[i][j-1])==t[i][j]:
        if t[i-1][j]==t[i][j]:
            i-=1
        else:
            j-=1
    elif max(t[i-1][j],t[i][j-1])!=t[i][j]:
        result.append(val[i-1])
        j-=i
        i-=1

print(result)

list.in