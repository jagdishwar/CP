memo={}
def solve(s,i,j):
    if i>=j:
        return 0
    if s[i:j+1]==s[i:j+1][::-1]:
        return 1
    if (i,j) in memo:
        return memo[(i,j)]
    mn=float('inf')
    for k in range(i,j+1):
        memo[(i,j)]=1+solve(s,i+1,k)+solve(s,k+1,j)
        mn=min(mn,memo[(i,j)])
    memo[(i,j)]=mn
    return memo[(i,j)]
s="kwtbjmsjvbrwriqwxadwnufplszhqccayvdhhvscxjaqsrmrrqngmuvxnugdzjfxeihogzsdjtvdmkudckjoggltcuybddbjoizu"
i=0
j=len(s)-1
value=solve(s,i,j)
print(value)
