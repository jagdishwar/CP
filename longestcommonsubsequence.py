strx="abdcd"
stry="afhcde"
m=len(strx)
n=len(stry)
memo={}

def lcs(strx,stry,m,n):
    if n==0 or m==0:
        return 0
    if (n,m) in memo:
        return memo[(n,m)]
    if strx[n-1]==stry[m-1]:
        memo[(n,m)]=1+lcs(strx,stry,m-1,n-1)
        return memo[(n,m)]
    else:
        memo[(n,m)]=max(lcs(strx,stry,m,n-1),lcs(strx,stry,m-1,n))
        return memo[(n,m)]

result=lcs(strx,stry,n,m)
print(result)

##table approach

t=[]
for i in range(len(strx)+1):
    list2=[]
    for j in range(len(stry)+1):
        list2.append(0)
    t.append(list2)

for i in range(1,len(strx)+1):
    for j in range(1,len(stry)+1):
        if strx[i-1]==stry[j-1]:
            t[i][j]=1+t[i-1][j-1]
        else:
            t[i][j]=max(t[i][j-1],t[i-1][j])

print(t[-1][-1])


############printing elements
i=len(strx)
j=len(stry)
list1=[]
while i>0 and j>0:
    if strx[i-1]==stry[j-1]:
        list1.append(strx[i-1])
        i-=1
        j-=1
    else:
        if t[i-1][j]>t[i][j-1]:
            i-=1
        else:
            j-=1

print(''.join(list1[::-1]))













