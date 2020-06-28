list1=[0,4,12,2,10,6,9,13,3,11,7,15]
maxlenght=[1]*(len(list1))
indexs=['start']
j=0
i=1

index=0
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


print(maxlenght)
print(indexs)