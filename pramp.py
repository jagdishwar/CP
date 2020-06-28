str1="GEEEKSFORGEEK"
list1=list(str1)
row=0
col=0
limit=3
str2=''
matrix=[]
for i in range(3):
    list3=[]
    for j in range(len(str1)):
        list3.append(0)
    matrix.append(list3)

for j in range(len(str1)):
    count=0
    var1=2
    var2=1
    if count<3 and var1!=var2:
        for k in range(3):
            if count==k:
               matrix[k][j]=str1[j]
        count+=1
        var1+=1
    if count>=2:
        count=2
    if count==2 and var1!=var2:
        for p in range(2,-1,-1):
            matrix[p][j]=str1[j]
            print(str1[j])
        count-=1
        var2+=1
print(matrix)



