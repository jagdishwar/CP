def generateallparanthesis(output,n,combination,l,r):
    if (len(combination)==n*2):
        output.append(''.join(combination[:]))
        return
    if l<n:
        combination.append('(')
        generateallparanthesis(output,n,combination,l+1,r)
        combination.pop()
    if r<l:
        combination.append(')')
        generateallparanthesis(output,n,combination,l,r+1)
        combination.pop()

output=[]
n=3
generateallparanthesis(output,n,[],0,0)
print(output)