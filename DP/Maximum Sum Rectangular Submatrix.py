def kadanealgo(list1):
    maxvalue=-float('inf')
    sum1=0
    value=-float('inf')
    result=0
    for i in list1:
        sum1+=i

        if sum1<=0:
            value=max(value,sum1)
            sum1=0

        maxvalue=max(maxvalue,sum1)

    if maxvalue>0:
        result=maxvalue
    else:
        result=value

    return result

matrix=[[-2]]
maxvalue=-float('inf')

for k in range(len(matrix[0])):
    list1 = [0] * len(matrix)
    for j in range(k,len(matrix[0])):

        for i in range(len(matrix)):
            ele=matrix[i][j]
            list1[i]+=ele

    maxval=kadanealgo(list1)
    print(maxval)
    maxvalue=max(maxval,maxvalue)

print(maxvalue)
