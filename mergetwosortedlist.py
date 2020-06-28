list1=[1,5,8]
list2=[6,9]
list3=[]
i=0
j=0
while i<=len(list1)-1 and j<=len(list2)-1:
    if list1[i]<list2[j]:
        list3.append(list1[i])
        i+=1
    elif list1[i]>list2[j]:
        list3.append(list2[j])
        j+=1

print(i,j)
while i<len(list1):
    list3.append(list1[i])
    i+=1
while j<len(list2):
    list3.append(list2[j])
    j+=1
print(list3)