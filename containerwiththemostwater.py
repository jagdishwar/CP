list1=[1, 5, 4, 3]

print(list1)
i=0
j=len(list1)-1
maxvalue=0
while i<j:
   if list1[i]<list1[j]:
       maxvalue=max(maxvalue,list1[i]*(j-i))
       i+=1
   else:
       maxvalue=max(maxvalue,min(list1[j]*(j-i))
       j-=1





print(maxvalue)
