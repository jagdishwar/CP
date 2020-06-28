list1=[-1,2,1,-4]
target=1
i=0
j=1
k=2
mindistance=float('inf')
for i in range(len(list1)):
    j=i+1
    while i<len(list1) and j<len(list1) and k<len(list1):
        add = (abs(list1[i]+list1[j]+list1[k])-target)
        if add < mindistance :
            mindistance=add
        if k==len(list1)-1:
            j+=1
            k=j+1
        if j==len(list1)-1:
            break
        k+=1
print(mindistance)






