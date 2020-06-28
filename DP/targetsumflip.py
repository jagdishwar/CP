list1=[1,1,2,3]
target=1
#s1-s2=diff
#s1+s2=sum1
#2s1=diff+sum1
#s1=(diff+sum1)//2
s1=(target+sum(list1))//2
t=[]
for i in range(len(list1)+1):
    list2=[]
    for j in range(s1+1):
        list2.append(0)
    t.append(list2)

for i in range(len(list1)+1):
    t[i][0]=1

for i in range(1,len(list1)+1):
        for j in range(1,s1+1):
            if list1[i-1]<=j:
                t[i][j]=t[i-1][j-list1[i-1]] + t[i-1][j]
            elif list1[i-1]>j:
                t[i][j]=t[i-1][j]

print(t[-1][-1])

