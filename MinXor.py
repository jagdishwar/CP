list1 = [0, 2, 5, 7]
list1.sort()
low=0
high=1
minxorvalue=float('inf')
while high<=len(list1)-1:
    value=list1[low]^list1[high]
    if minxorvalue>value:
         minxorvalue=value
    low+=1
    high+=1

print(minxorvalue)