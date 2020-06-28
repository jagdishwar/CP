"""list1= [ "cat", "dog", "god", "tca" ]
setdict=[dict() for i in range(len(list1))]
resultlist=[]
resultdict=Ordedict
for i in range(len(list1)):
    for j in list1[i]:
        if j in setdict[i]:
            setdict[i][j]+=1
        else:
            setdict[i][j]=1

for i in range(len(setdict)):
    if [setdict[i]] in resultdict:
        resultdict[setdict[i]]+=1
    else:
        resultdict[setdict[i]]=1


print(resultlist)
"""
list1=['cat','dog','god','tca']
cat='cat'
li=sorted(cat)
print(li)
list1=[2,3,41,324,1]
list1=sorted(list1)
print(list1)