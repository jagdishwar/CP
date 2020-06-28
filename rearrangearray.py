list1=[ 4, 0, 2, 1, 3 ]
listt1=str(list1)
print(list1)
temp=[0 for i in range(len(list1))]
for i in range(len(list1)):
    temp[list1[i]-1]=i
print(temp)

