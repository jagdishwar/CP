list1=[ 21, 1, 45, 10, 33 ]
for i in range(len(list1)):
    minpos=i
    for j in range(i+1,len(list1)):
        if list1[j]<list1[minpos]:
            list1[minpos],list1[j]=list1[j],list1[minpos]

minvalue=0
print(list1)
for i in range(1,len(list1)):
           k=list1[i]-list1[i-1]
           if k>minvalue:
               minvalue=k


print(minvalue)