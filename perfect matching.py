list1=[[2,3]]
list2=[[1],[2],[2]]


matrix1=[[i+1,list1[i][j],0,0] for i in range(len(list1)) for j in range(len(list1[i]))]
matrix2=[[i+1,list2[i][j],0,0] for i in range(len(list2)) for j in range(len(list2[i]))]
print(matrix1)
print(matrix2)
m=3
n=3
status = 0
flag=0
def factorial(num):
    sum1=1
    for i in range(1,num+1):
        sum1*=i
    return sum1
print(factorial(m*n))
for loop in range(factorial(m*n)):
    count1=0
    count2=0
    i=0
    j=0
    ctrl=0
    for u in range(len(matrix1)):
        matrix1[u][3]=0
    for v in range(len(matrix2)):
        matrix2[v][3]=0

    while i<len(matrix1) or j<len(matrix2):
        print(i,j,"ctrl",ctrl)
        if i==len(matrix1):
            if ctrl==0:
                ctrl=1
            else:
                j+=1


        if ctrl==0 and matrix1[i][1]-1<len(matrix2) and matrix2[matrix1[i][1]-1][3]==0 and matrix1[i][2]==0 and matrix1[i][3]==0:
            if  matrix2[matrix1[i][1]-1][1]-1<len(matrix1) and matrix2[matrix1[i][1]-1][1]==matrix1[i][0]  and matrix1[matrix2[matrix1[i][1]-1][1]-1][3]==0:
                matrix2[matrix1[i][1]-1][2]=1
            matrix1[i][2] = 1
            matrix1[i][3] = 1
            matrix2[matrix1[i][1]-1][3]=1
        if ctrl==1 and matrix2[j][1]-1<len(matrix1) and matrix1[matrix2[j][1]-1][3]==0 and matrix2[j][2]==0 and matrix2[j][3]==0:
            if matrix1[matrix2[j][1]-1][1]-1<len(matrix2) and matrix1[matrix2[j][1] - 1][1] == matrix2[j][0]  and matrix2[matrix1[matrix2[j][1]-1][1]-1][3]==0:
                matrix1[matrix2[j][1] - 1][2] = 1
            matrix2[j][2] = 1
            matrix2[j][3] = 1
            matrix1[matrix2[j][1]-1][3] = 1


        print(matrix1)
        print(matrix2)

        if i!=len(matrix1):
            i+=1
            ctrl=0


    if flag==0 or flag==2:
            for s1 in range(len(matrix1)):
                if status == 0 or status == 1:

                    if matrix1[s1][2]==1:
                        count1+=1
                    if count1 == len(matrix1):
                        status += 1
                        flag=1
    if flag==0 or flag==1:
            for s2 in range(len(matrix2)):
                if status == 0 or status == 1:

                    if matrix2[s2][2]==1:
                        count2+=1
                    if count2==len(matrix2):
                        status+=1
                        flag=2

    if status==2:
        print(loop+1)
        break








