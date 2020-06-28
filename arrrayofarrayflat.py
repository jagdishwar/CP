matrix=[[1,2,4,45],[234,3434,234,23],[234,2341,1,34]]
list1=[]
for i in matrix:
    for j in i:
        list1.append(j)

print(list1)
list1=[1,2,3,4,4,[34,[32,3,[2]]]]
while list1:
   ele = list1.pop()
   if ele is list:
       for i in ele:
           print(i)
   else:
       print(ele)
