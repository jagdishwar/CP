list1=[1, 4, 10]
list2=[2, 15, 20]
list3=[10, 12]
i=len(list1)-1
j=len(list2)-1
k=len(list3)-1
minvalue=float('inf')
x,y,z=0,0,0
while i > -1 and j > -1 and k > -1:
    value=abs(max(list1[i],list2[j],list3[k])-min(list1[i],list2[j],list3[k]))
    if value<minvalue:
        minvalue=value
        x=list1[i]
        y=list2[j]
        z=list3[k]

    maxvalue=max(list1[i],list2[j],list3[k])
    if maxvalue==list1[i]:
        i-=1
    elif maxvalue==list2[j]:
        j-=1
    else:
        k-=1



print(minvalue)
print(x,y,z)