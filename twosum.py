list1=[2, 7, 11, 15]
target=9
dict1={}
for i in range(len(list1)):
     complement=target-list1[i]
     if complement not in dict1:
         dict1[list1[i]]=i
     elif A[i] not in dict1:
         print(dict1[complement],i)


print(dict1)