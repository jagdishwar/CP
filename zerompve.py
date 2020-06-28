list1=[0,1,0,3,12]
i,j=0,0
while i<len(list1) and j<len(list1):
    if list1[j]!=0:
        if list1[i]==0:
           list1[i], list1[j] = list1[j], list1[i]
           i+=1
    j+=1

print(list1)