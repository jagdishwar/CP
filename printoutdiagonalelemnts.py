matrix=[[12,3,123,342,32],[23,45,2,32,24],[234,246,21,1,34],[234,21,2,5412,12]]

list2=[]
m,n=4,5
for i in range(m):
    k=i
    j=0
    list1 = []
    while (k>=0):

        list1.append(matrix[j][k])
        k-=1
        j+=1
    list2.append(list1)
for i in range(1,m):
    f=i
    p=n-1
    list1 = []
    while (p>=1)and (f<=m-1):
        list1.append(matrix[f][p])
        p-=1
        f+=1
    list2.append(list1)


print(list2)