list1=[ 1, 11, 12 ]
list1.sort()
count=0
list2=[]
list4=[]
for i in range(len(list1)):
    left=i+1
    right=left+1
    list2=[]
    while right<=len(list1)-1 and left<=len(list1)-1:
        if list1[left]+list1[right]>list1[i]:
            count+=1
            list2.append([list1[i],list1[left],list1[right]])
        if right==len(list1)-1 :
            left+=1
            right=left+1
        right+=1
    list4.append(list2)
print(count)
print(len(list4)-1)