list1=[4,1,1,2,1,3]
dict1={}
b=1
for i in range(len(list1)):
    if list1[i] in dict1:
        dict1[list1[i]]+=1
    else:
        dict1[list1[i]]=1
print(dict1)
list3=[]
for key,value in dict1.items():
    if value==b:
        list3.append(key)

print(list3)
