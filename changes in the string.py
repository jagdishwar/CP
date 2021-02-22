strx="JADISHWAR is my brother gdfgd"
stry="SARVESHWAR is my brother"
t=[[0 for i in range(len(stry)+1)] for j in range(len(strx)+1)]
list1=set()
for i in range(1,len(strx)+1):
    for j in range(1,len(stry)+1):
        if strx[i-1]==stry[j-1]:
            t[i][j]=1+t[i-1][j-1]
            list1.add(i-1)

        else:
            t[i][j]=max(t[i-1][j],t[i][j-1])

box=[]
for i in range(len(strx)):
    if i not in list1:
        box.append(i)

list1=box
result=[list1[0]]
tube=[]
for i in range(1,len(list1)):
    if result[-1]+1==list1[i]:
        result.append(list1[i])
        continue
    else:
        tube.append((result[0],result[-1]))
        del result[:]
        result.append(list1[i])
if len(result)>0:
    tube.append((result[0],result[-1]))
print(list(set(tube)))




