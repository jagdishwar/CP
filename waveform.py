list1=[2,3,4,34,5,26,7,25,41]
list1.sort()

for i in range(len(list1)-1):
    if i%2==0:
        if not (list1[i]>list1[i+1]):
            list1[i],list1[i+1]=list1[i+1],list1[i]
    else:
        if not(list1[i]<list1[i+1]):
            list1[i],list1[i+1]=list1[i+1],list1[i]


print(list1)