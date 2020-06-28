list1=[-2]
sum1=0
value=0
for i in range(len(list1)):
    value+=list1[i]
    if value<0:
        value=0
    elif sum1<value:
        sum1=value

if abs(sum(list1))>sum1:
    return sum(list1)
else:
    return sum1