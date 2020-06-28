list1=[1,3,4,5,1,45]
set1=set(list1)
list2=list(set1)
print(list1)
print(list2)
sum1=sum(list1)
sum2=sum(list2)

if sum1!=sum2:
    return sum1-sum2
else:
    return -1

