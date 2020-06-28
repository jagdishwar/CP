list1=[1,2,3,3,4,5,6]
list2=[3,3,5]
list3=[]
listmax=[]

if len(list1)<len(list2):
    list3=list1
    listmax=list2
else:
    list3=list2
    listmax=list1
dict1={}
for i in range(len(listmax)):
    if (listmax[i]) in dict1:
        dict1[(listmax[i])]+=1
    else:
        dict1[listmax[i]]=1
lisy=[]
for i in range(len(list3)):

    if list3[i] in dict1:

        lisy.append(list3[i])
        dict1[list3[i]]-=1




print(lisy)
