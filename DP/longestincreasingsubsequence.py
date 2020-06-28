list1= [1, 11, 2, 10, 4, 5, 2, 1]
                  #     [0, 1,  2,  3, 4, 5,6, 7,9]
                  #    [1,2,4,5],[11,10,5,2,1]
maxlenght=[1]*(len(list1))
indexs=['start']
j=0
i=1

index=0
maxvalue=0
while i<len(list1):
                    maxvalue = 0
                    for j in range(i):
                        if list1[j]<list1[i]:
                            if maxlenght[j]>=maxvalue:
                                maxvalue=maxlenght[j]
                                index=j
                    maxlenght[i]=maxvalue+1
                    indexs.append(index)
                    i+=1

maxvalueindex=maxlenght.index(max(maxlenght))

                j=indexs[maxvalueindex]
                merge1=[maxvalueindex]
                for i in range(maxvalueindex-1,-1,-1):
                    if j==i:
                        merge1.append(i)
                        j=indexs[i]



list1=[1, 11, 2, 10, 4, 5, 2, 1]

maxlenght=[1]*(len(list1))
indexs=['start']
j=0
i=1

while i<len(list1):
    maxvalue = 0
    for j in range(i):
        if list1[j]>list1[i]:
            if maxlenght[j]>=maxvalue:
                maxvalue=maxlenght[j]
                index=j
    maxlenght[i]=maxvalue+1
    indexs.append(index)
    i+=1

maxvalueindex=maxlenght.index(max(maxlenght))

j=indexs[maxvalueindex]
merge2=[maxvalueindex]
for i in range(maxvalueindex-1,0,-1):
    if j==i:
        merge2.append(i)
        j=indexs[i]



merge1=merge1[::-1]
merge2=merge2[::-1]


#     [0, 1,  2,  3, 4, 5,6, 7,9]
  #    [1,2,4,5],[11,10,5,2,1]
mindiff=float('inf')
chop1=0
chop2=0
for i in range(len(merge1)):
    for j in range(len(merge2)):
        if merge1[i]-merge2[j]<mindiff:
            mindiff=merge1[i]-merge2[j]
        if merge1[i]-merge2[j]==0:
            break
    chop1=i
    chop2=j

result=merge1[:i]+merge2[j:]
gplist=[list1[i] for i in result]
print(gplist)