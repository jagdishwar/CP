for _ in range(T):
    count = 0
    maxele = -float('inf')
    list1 = V.split(' ')
    if list1[0] > list1[1]:
        count += 1
    for i in range(2, N):
        list1 = list(map(int, V.split(' ')))

        if list1[i - 1] < list1[i] > list1[i + 1] and maxele < list1[i]:
            count += 1
            maxele = max(maxele, list1[i])
    return (count)


