strx='heap'
stry='pea'
#heap---pea
# I \   / D
#   ea

#find Lcs
t=[]
t=[[0 for i in range(len(stry)+1)]for i in range(len(strx)+1)]
for i in range(1,len(strx)+1):
    for j in range(1,len(stry)+1):
        if strx[i-1]==stry[j-1]:
            t[i][j]=1+t[i-1][j-1]
        else:
            t[i][j]=max(t[i-1][j],t[i][j-1])

num=(len(strx)-t[-1][-1])+(len(stry)-t[-1][-1])
print(num)