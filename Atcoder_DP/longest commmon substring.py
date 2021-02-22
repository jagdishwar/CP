strx='hello'
stry='elox'
def dp(i,j,count):
    if i>=len(strx) or j>=len(stry):
        return 0

    if strx[i]==stry[j]:
        return dp(i+1,j+1,count+1)
    else:
        return max(dp(i,j+1,0),dp(i+1,j,0),count)

print(dp(0,0,0))

