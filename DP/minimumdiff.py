#2sum1-s1=minimum
#find s1
t=[]
list1=[ 8, 4, 5, 7, 6, 2 ]
sum1=sum(list1)
for i in range(len(list1)+1):
    list2=[]
    for j in range(sum1+1):
        list2.append(True)
    t.append(list2)

for i in range(1,sum1+1):
    t[0][i]=False

for i in range(1,len(list1)+1):
    for j in range(1,sum1+1):
        if list1[i-1]<=j:
            t[i][j]=t[i-1][j-list1[i-1]]or t[i-1][j]
        elif list1[i-1]>j:
            t[i][j]=t[i-1][j]

suppose=[]
for i in range(sum1+1):
    if t[-1][i]==True:
        suppose.append(i)

print(suppose)
###minimum find out
mindiff=float('inf')
for i in range((len(suppose)//2)):
    if mindiff > (sum1 - (2 * (suppose[i]))):
        mindiff = (sum1 - (2 * (suppose[i])))
        s1 = suppose[i]

print(mindiff)

t=[]
list1=[ 8, 4, 5, 7, 6, 2 ]
sum1=s1
print(s1)
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
            t[i][j]=min(1+t[i-1][j-list1[i-1]],t[i-1][j])
        elif list1[i-1]>j:
            t[i][j]=t[i-1][j]
print(t[-1][-1])