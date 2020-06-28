list1=[2,3,4,5,6,46,8,9,10]
list2=[]
list4=[]

for i in range(len(list1)-2,-1,-1):
    list2.append(list1[i])

for k in range(len(list1)-1,7,-1):
    list2.append(list1[k])

for l in range(len(list2)-1,-1,-1):
    list4.append(list2[l])


print(list4)


