t=[]
#
wt=[20,10,30,40]
val=[5,10,30,20]
W=100
def unboundedknapsack(val,wt,W,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]<=W:
        return max(val[n-1]+unboundedknapsack(val,wt,W-wt[n-1],n),unboundedknapsack(val,wt,W,n-1))
    elif wt[n-1]>W:
        return unboundedknapsack(val,wt,W,n-1)

print(unboundedknapsack(val,wt,W,len(wt)))
t = []
for i in range(0, len(wt) + 1):
    list1 = []
    for j in range(0, W + 1):
        list1.append(0)
    t.append(list1)
k=2
counter=[0]*len(wt)
for i in range(1, len(wt) + 1):
    count=0
    for j in range(1, W + 1):
        if count == k:
            break
        elif wt[i - 1] <= j:
            t[i][j] = max((val[i - 1] + t[i][j - wt[i - 1]]), t[i - 1][j])
        elif wt[i - 1] > j:
            t[i][j] = t[i - 1][j]
        count+=1

print(max(t))
weights=wt
capacity=W
dp=t
idxes_list = []
print("Selected weights are: ", end='')
n = len(weights)
x = n
y = capacity

while x > 0 and y > 0:
        if dp[x][y]==dp[x-1][y]:
            x-=1
        if (dp[x - 1][y] >= dp[x][y - wt[x - 1]] + val[x - 1]):
           x-=1
        else:
            print( wt[x - 1] , val[x - 1])
            y-=wt[x - 1]
weights = [weights[idx] for idx in idxes_list]

print(t[-1][-1])
"""################SO NEW FORMET HAVING CHANGE i=====i-1
if list1[i-1]<=j:
    t[i][j]=max((val[i-1]+t[i][j-list1[i-1]]),t[i-1][j])

elif list1[i-1]>j:
    t[i][j]=t[i-1][j]"""