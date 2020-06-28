str1='10.2.4'
list1=list(map(int,str1.split('.')))
print(list1)
for i in list1:
    print(type(i))