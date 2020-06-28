list1=[]
list2=[ -35, -16, 25, 36, 37, 46 ]
list3=list1+list2
list3.sort()
print(list3)
if len(list3)%2!=0:
    mid=len(list3)//2
    list3[mid]
else:
    mid=len(list3)//2
    has=mid-1
    print(list3[mid],list3[has])
    print((list3[mid]+list3[has])/2)