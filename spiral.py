count=0

matrix=[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

for i in range(len(matrix[0])):
    count+=1
m,n=len(matrix)-1,count-1
last_row=m
last_col=n
list2=[]
k=0
l=0
while (k<=last_row and l<=last_col):
    for i in range(last_col+1):
        list2.append(matrix[k][i])
    k+=1
    for i in range(k,last_row+1):
        list2.append(matrix[i][last_col])
    last_col-=1
    for i in range(last_col,l-1,-1):
        list2.append(matrix[last_row][i])
    last_row-=1
    for i in range(last_row,k-1,-1):
        list2.append(matrix[i][l])
    l+=1

print(list2)