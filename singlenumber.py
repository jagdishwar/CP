list1=[2,3,4,4,3]
dict1={}
for i in range(len(list1)):
    if list1[i] in dict1:
        dict1[list1[i]]+=1
    else:
        dict1[list1[i]]=1
for key,value in dict1.items():
    if value==1:
        print(key)