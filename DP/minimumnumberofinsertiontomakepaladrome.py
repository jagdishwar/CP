strx="aebcbda"
stry=strx[::-1]
#deletion is same insertion
t=[[0 for i in range(len(stry)+1)] for j in range(len(strx)+1)]
for i in range(1,len(strx)+1):
    for j in range(1,len(stry)+1):
        if strx[i-1]==stry[j-1]:
            t[i][j]=1+t[i-1][j-1]
        else:
            t[i][j]=max(t[i-1][j],t[i][j-1])

print(len(strx)-t[-1][-1])