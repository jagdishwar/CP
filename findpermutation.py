n=3
s="ID"
list1=[]
for i in range(1,n+1):
    list1.append(i)
list2=[]
value=0


for i in s:
        if 'D' is i:
            print(i)
            value=list1[-1]
            list2.append(value)
            list1.remove(value)
            print(list1,'list1')
            print(list2,'list2')
        if 'I' is i:
            print(i,'I')
            value=list1[0]
            list2.append(value)
            list1.remove(value)
            print(list1,'list`111')
print(list2+list1)
