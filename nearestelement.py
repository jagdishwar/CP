list1=[ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
result=[]
queue=[]

for num in list1:
    while queue and queue[-1]>=num:
        queue.pop()
    if queue:
        result.append(queue[])
    else:
        result.append(-1)
    queue.append(num)
print(result)

