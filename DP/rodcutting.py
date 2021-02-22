n=8
list1=[]
for i in range(1,n+1):
    list1.append(i)
val=[1,3,2,5,2,8,4,6]
print(list1)
t=[]
for i in range(len(list1)+1):
    list2=[]
    for j in range(n+1):
        list2.append(0)
    t.append(list2)

print(t)
for i in range(1,len(list1)+1):
    for j in range(1,n+1):
        if list1[i-1]<=j:
            t[i][j]= max(val[i-1]+t[i][j-list1[i-1]],t[i-1][j])
        elif list1[i-1]>j:
            t[i][j]=t[i-1][j]

print(t[-1][-1])