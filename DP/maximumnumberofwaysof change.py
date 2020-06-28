#unlimited no. of coins are available
list1=[1,2,5]
sum1=11
t=[]
for i in range(len(list1)+1):
    list2=[]
    for j in range(sum1+1):
        list2.append(0)
    t.append(list2)
for i in range(len(list1)+1):
    t[i][0]=1

for i in range(1,len(list1)+1):
    for j in range(1,sum1+1):
        if list1[i-1]<=j:
            t[i][j]= t[i][j-list1[i-1]] + t[i-1][j]
        elif list1[i-1]>j:
            t[i][j]=t[i-1][j]


print(t[-1][-1])

