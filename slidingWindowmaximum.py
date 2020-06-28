A=[1, 3, -1, -3, 5, 3, 6, 7]
B=3
if B>=len(A):
    print(max(A))

queue=[]
result=[]
for i in range(len(A)):
    if queue and queue[0]==i-B :
        del queue[0]
    while queue and A[queue[-1]]<A[i]:
        del queue[-1]
    queue.append(i)
    if i+1>=B:
        result.append(A[queue[0]])

print(result)


