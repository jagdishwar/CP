data=[ [1487799425, 14, 1],
                 [1487799425, 4,  0],
                 [1487799425, 2,  0],
                 [1487800378, 10, 1],
                 [1487801478, 18, 0],
                 [1487801478, 18, 1],
                 [1487901013, 1,  0],
                 [1487901211, 7,  1],
                 [1487901211, 7,  0] ]
n = len(data)
timestamp = None
max_people = 0
current_count = 0
for i in range(n):
    if data[i][2] == 1:
        current_count += data[i][1]
    elif data[i][2] == 0:
        current_count -= data[i][1]
    print(i,'without skipping')
    if i < n - 1 and data[i][0] == data[i + 1][0]:
        continue
    print(current_count)
    print('after skipping',i)
    if current_count > max_people:
        max_people = current_count
        timestamp = data[i][0]
print(timestamp)