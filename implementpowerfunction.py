list1=[]
def binary(num):
    if num==0:
        return 0

    binary(num//2)
    list1.append(num%2)

x,num,d=abs(-1),1,20
list2=[]
binary(num)
if list1[0]==1:
    base=x
    list2.append(base)
list3=list1[1:]
for i in list3:
    if i ==1:
        popup=list2.pop()
        value=(popup**2)%d
        fri=(base*value)%d
        list2.append(fri)
    else:
        popup=list2.pop()
        value=(popup**2)%d
        list2.append(value)



print(list2)
