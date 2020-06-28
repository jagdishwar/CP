values={0:0}
list1=[1,2,2,-4,-1,10]
sumcount=0
s,e=-1,-1
for i in range(len(list1)):
    sumcount+=list1[i]
    if sumcount not in values:
        values[sumcount]=i+1
    elif i-values[sumcount]>e-s:
        s=values[sumcount]
        e=i

print(list1[s:e+1])