import math
import collections
def setlimit(strlen):
    l=math.floor(math.sqrt(strlen))
    r=math.ceil(math.sqrt(strlen))
    minvalue=0
    row=0
    col=0
    i=l
    j=l
    while i<=r and j<=r:
        if i*j>=strlen:
            minvalue=i*j
            row=i
            col=j
            break
        if j==r:
            i+=1
            j=i

        if j!=r:
            j+=1
    return (row,col)

string="its harder to read code than to write it"
strlen=0
oristr=""
collections.deque(list(oristr))
for i in string:
    if i!=' ':
        strlen+=1
        oristr+=i
print(oristr)
row,col=setlimit(strlen)
queue=collections.deque(list(oristr))
print(row,col)
print(queue)

matrix=[['#']*col for i in range(row)]
print(matrix)
for i in range(row):
    for j in range(col):
        if len(queue)>=1:
            matrix[i][j]=queue.popleft()

print(queue)
print(matrix)
result=""
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        if matrix[i][j]!='#':
            result+=matrix[i][j]
    result+=' '
print(result)
