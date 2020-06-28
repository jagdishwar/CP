list1=[7,6,4,3,1]
profit=0
for i in range(1,len(list1)):
    if list1[i-1]<list1[i]:
        profit+=list1[i]-list1[i-1]

print(profit)
