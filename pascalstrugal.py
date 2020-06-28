row=5

list1 = [1,1]
list2=[]

for i in range(row):
    add=0
    for j in range(i+1):
        if i==j :
            if j-1>=0:
                add=list1[j]+list1[j-1]
                list1.extend(add)
    list2.extend(list1)



print(list2)
