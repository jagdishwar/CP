list1=[3, 4, 7, 1, 2, 9, 8]
setdict={}
result=[]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        k=list1[i]+list1[j]
        if k in setdict:
            if setdict[k][0]!=i and setdict[k][1]!=i and setdict[k][0]!=j and setdict[k][1]!=j:
                result.append(list(setdict[k])+[i]+[j])
        else:
            setdict[k]=(i,j)


if not result :
     print(result)

print(result)
result.sort()
print(result)
print(sorted(result)[0])