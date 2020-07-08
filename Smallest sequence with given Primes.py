list1=[-3,6,-6,3]
def kadanealgo(list1):
    set1=set()
    sum1=0
    count=0
    for i in list1:
        sum1+=i

        if sum1==0:
            count+=1
        elif sum1 in set1:
            count+=1
        set1.add(sum1)
    return(count)
matrix=[[-8,5,7],
        [3,7,-8],
        [5,-8,9]]
maxvalue=0
for k in range(len(matrix[0])):
    list1 = [0] * len(matrix)
    for j in range(k, len(matrix[0])):
        for i in range(len(matrix)):
            ele = matrix[i][j]
            list1[i] += ele
        print(list1)
        maxval = kadanealgo(list1)

        maxvalue += maxval

print(maxvalue)

