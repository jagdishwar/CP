a=3
b=3
list2=[]
for i in range(3):
    list1=[]
    for j in range(3):
        list1.append(1)
    list2.append(list1)


print(list2)
for i in range(1,3):
    for j in range(1,3):
        list2[i][j]=list2[i-1][j]+list2[i][j-1]

print(list2[-1][-1])
list4=[2,3,4,21,51,5]
import numpy as np
matrix=np.array(list4).reshape(3,2)
print(matrix)


