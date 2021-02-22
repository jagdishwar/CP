h
strx="afdf"
stry='fdf'
def dp(i,j):
    if i>=len(strx) or j>=len(stry):
        return 0

    if strx[i]==stry[j]:
        return 1+dp(i+1,j+1)
    else:
        return max(dp(i,j+1),dp(i+1,j))

print(dp(0,0))

strx=input()
stry=input()
#converstion into tabular
dp=[[0 for i in range(len(stry)+1)] for j in range(len(strx)+1)]

for i in range(1,len(strx)+1):
    for j in range(1,len(stry)+1):
        if strx[i-1]==stry[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])


#printing out the string
i=len(strx)
j=len(stry)
result=""

while i>0 and j>0:
        if dp[i][j-1]==dp[i][j]:
            j-=1
        elif dp[i-1][j]fgg==dp[i][j]:
            i-=1
        else:
            result+=strx[i-1]
            i-=1
            j-=1
print(result[::-1])




