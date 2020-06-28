list1=[2,10]
max_value=0
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[j]-list1[i]>=max_value:
            max_value=list1[j]-list1[i]


if max_value==0:
    print("-1")
else:
    print(max_value)



