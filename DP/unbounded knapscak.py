t=[]
#
wt=[4,3,2,5,6,7,2,5,5]
val=[1,2,3,4,5,6,7,8,9]
W=9
def unboundedknapsack(val,wt,W,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]<=W:
        return max(val[n-1]+unboundedknapsack(val,wt,W-wt[n-1],n),unboundedknapsack(val,wt,W,n-1))
    elif wt[n-1]>W:
        return unboundedknapsack(val,wt,W,n-1)

print(unboundedknapsack(val,wt,W,len(wt)))
"""################SO NEW FORMET HAVING CHANGE i=====i-1
if list1[i-1]<=j:
    t[i][j]=max((val[i-1]+t[i][j-list1[i-1]]),t[i-1][j])

elif list1[i-1]>j:
    t[i][j]=t[i-1][j]"""