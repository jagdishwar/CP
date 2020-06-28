t=[]
list1=[15, 10, 6]
sum1=15
for i in range(len(list1)+1):
    list2=[]
    for j in range(sum1+1):
        list2.append(0)
    t.append(list2)

for i in range(sum1+1):
    t[0][i]=float('inf')

for j in range(1,sum1+1):

    if j%list1[1-1]==0:
        t[1][j]=j//list1[1-1]
    else:
        t[1][j]=float('inf')

for i in range(2,len(list1)+1):
    for j in range(1,sum1+1):
        if list1[i-1]<=j:
            t[i][j]= min(1+t[i-1][j-list1[i-1]],t[i-1][j])
        elif list1[i-1]>j:
            t[i][j]=t[i-1][j]

print(t[-1][-1])
