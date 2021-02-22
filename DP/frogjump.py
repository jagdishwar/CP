jump_cost=[8, 1, 2, 3, 4]
n=len(jump_cost)
memo={}
minvalue=float('inf')
def dfsdeploy(i,mivalue):
        if i>=n-1:
            return 0
        if i in memo:
            return memo[i]
        minvalue=float('inf')
        left=dfsdeploy(i+1,minvalue)+abs(jump_cost[i]+jump_cost[i+1])
        right=float('inf')
        if i+2<n:
            right=dfsdeploy(i+1,minvalue)+abs(jump_cost[i]+jump_cost[i+2])
        minvalue=min(minvalue,min(left,right))
        print(minvalue)
        return min(left,right)


print(dfsdeploy(0,minvalue))
print(minvalue)