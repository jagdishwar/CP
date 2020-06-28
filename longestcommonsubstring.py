strx="abciiidef"
stry="aeiou"
t=[]
for i in range(len(strx)+1):
    list2=[]
    for j in range(len(stry)+1):
        list2.append(0)
    t.append(list2)

for i in range(1,len(strx)+1):
    for j in range(1,len(stry)+1):
        if strx[i-1]==stry[j-1]:
            t[i][j]=1+t[i][j]
        else:
            t[i][j]=0
maxvalue=0
print(t[-1][-1])
for i in range(len(strx)+1):
    for j in range(len(stry)+1):
        maxvalue=max(maxvalue,t[i][j])
print(maxvalue)
