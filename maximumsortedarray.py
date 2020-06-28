list1 =[1, 3, 2, 4, 5]
list2=[]
for i in list1:
    list2.append(i)
list1.sort()
for i in range(len(list1)):
    if list1[i]!=list2[i]:
        return(list2[i-1],list2[i+1])
        break

return (-1)







