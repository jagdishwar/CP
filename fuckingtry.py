list1 = [ 8, 4, 5, 7, 6, 2 ]
# s1-s2=minimum
# s2=sum1-s1
# sum1-2s1=minimum
t = []
sum1 = sum(list1)
for i in range(len(list1) + 1):
    list2 = []
    for j in range(sum(list1) + 1):
        list2.append(False)
    t.append(list2)

for i in range(len(list1) + 1):
    t[i][0] = True
for i in range(1, len(list1) + 1):
    for j in range(1, sum(list1) + 1):
        if list1[i - 1] <= j:
            t[i][j] = t[i - 1][j - list1[i - 1]] or t[i - 1][j]
        elif list1[i - 1] > j:
            t[i][j] = t[i - 1][j]

list2 = []

for i in range(sum(list1) + 1):
    if t[-1][i] == True:
        list2.append(i)
mindiff = float('inf')

s1 = 0

for i in range(len(list2) // 2):
    if mindiff > (sum1 - (2 * (list2[i]))):
        mindiff = (sum1 - (2 * (list2[i])))
        s1 = list2[i]

###count the subset having sum == s1
print(s1)

t=[]
list1=[ 8, 4, 5, 7, 6, 2 ]
sum1=s1
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




