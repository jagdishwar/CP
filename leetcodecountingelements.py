list1=[1,2,3]
data={}
count=0
for i in list1:
    if i in data:
        data[i]+=1
    else:
        data[i]=1
for i in list1:
    if i+1 in data and data[i+1]!=0:
        count+=1
        data[i+1]-=1

print(count)
