t=[]
#
n,k,a=map(int,input().split())

wt=list(map(int,input().split()))
val=list(map(int,input().split()))
print(wt)
print(val)
listprofit=[]
for i in range(len(val)):
    listprofit.append((wt[i]*val[i])/100)
W=a
count=k
print(listprofit)
def unboundedknapsack(val,wt,W,n,count):
    if n==0 or W==0 :
        return 0
    if wt[n-1]<=W:
        return max((listprofit[n-1]*val[n-1])+unboundedknapsack(val,wt,W-wt[n-1],n,count-1),unboundedknapsack(val,wt,W,n-1,count))
    elif wt[n-1]>W:
        return unboundedknapsack(val,wt,W,n-1,count)

print(unboundedknapsack(val,wt,W,len(wt),count))

t = []
for i in range(0, len(wt) + 1):
    list1 = []
    for j in range(0, W + 1):
        list1.append(0)
    t.append(list1)
for i in range(1, len(wt) + 1):
    for j in range(1, W + 1):
        if wt[i - 1] <= j:
            t[i][j] = max((val[i - 1] + t[i][j - wt[i - 1]]), t[i - 1][j])
        elif wt[i - 1] > j:
            t[i][j] = t[i - 1][j]
print()
print(t[-1][-1])


"""################SO NEW FORMET HAVING CHANGE i=====i-1
if list1[i-1]<=j:
    t[i][j]=max((val[i-1]+t[i][j-list1[i-1]]),t[i-1][j])

elif list1[i-1]>j:
    t[i][j]=t[i-1][j]"""