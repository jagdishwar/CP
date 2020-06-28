memo={}
def solve(arr,i,j):
    if i>=j:
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    mn=float('inf')
    for k in range(i,j):
        memo[(i,j)]=solve(arr,i,k)+solve(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        mn=min(memo[(i,j)],mn)

    return mn
arr=[40,20,30,10,30]
i=1
j=len(arr)-1
value=solve(arr,i,j)
print(value)
