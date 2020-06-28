matrix=[   [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]   ]


l=0
k=0
lastcol=len(matrix[0])-1
count=0
for i in matrix:
    count+=1

lastrow=count-1
list1=[]

while k<=lastrow:
    for i in range(lastcol+1):
        value=matrix[k][i]
        if value == 0:
            list1.append([k,i])
    k+=1
for list2 in list1:
        p=list2[0]
        q=list2[1]
        for i in range(lastrow+1):
            matrix[p][i]=matrix[p][i]*0
        for i in range(lastcol+1):
            matrix[i][q]=matrix[i][q]*0





print(list1)
print(matrix)