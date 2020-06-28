def meragesort(list1):
    if len(list1)>1:
            mid=len(list1)//2
            left_list1=list1[:mid]
            right_list1=list1[mid:]
            meragesort(left_list1)
            meragesort(right_list1)
            i=0
            j=0
            k=0
            while i<len(left_list1) and j <len(right_list1):
                    if left_list1[i]<right_list1[j]:
                        list1[k]=left_list1[i]
                        i+=1
                        k+=1
                    else:
                        list1[k]=right_list1[j]
                        j+=1
                        k+=1
            while i<len(left_list1):
                list1[k] = left_list1[i]
                i += 1
                k += 1
            while j<len(right_list1):
                list1[k] = right_list1[j]
                j += 1
                k += 1


list1=[12,3,1,4,132]
meragesort(list1)
print(list1)