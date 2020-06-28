list1=[1,2,3]
print(list1.reverse())
inversepoint=len(list1)-2
while list1[inversepoint]>0 and list1[inversepoint]>list1[inversepoint+1]:
    inversepoint-=1

if inversepoint<0:
    print(list1)

for i in reversed(range(inversepoint,len(list1))):
    if list1[inversepoint]<list1[i]:
        list1[inversepoint],list1[i]=list1[i],list1[inversepoint]
        break

list1[inversepoint+1:]=reversed(list1[inversepoint+1:])

