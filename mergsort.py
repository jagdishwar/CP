list1=[ 1, 10, 5 ]
def meragesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left=list1[:mid]
        right=list1[mid:]
        meragesort(left)
        meragesort(right)
        i=j=k=0
        while i<(len(left)) and j <(len(right)):
            if left[i]<right[j]:
                list1[k] = left[i]
                i+=1
                k+=1
            else:
                list1[k] = right[j]
                j+=1
                k+=1
        while i<(len(left)):

                list1[k]=left[i]
                i += 1
                k+=1
        while j<len(right):
                list1[k] = right[j]
                j += 1
                k+=1
minvalue=0
meragesort(list1)
for i in range(1,len(list1)):
            k=list1[i]-list1[i-1]
            if k>minvalue:
                    minvalue=k





print(list1)