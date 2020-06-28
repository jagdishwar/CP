list1=[[1]]
k=5
for i in range(1,k):
    matrix=[1]
    for j in range(1,i):
        matrix.append(list1[i-1][j]+list1[i-1][j-1])
    matrix.append(1)
    list1.append(matrix)
print(list1.pop())