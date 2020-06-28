list1=[5,9,6,8,6,4,6,9,5,4,9]
max1=max(list1)
value=list1[max1]
index2=max1-1
index3=max1+1
mul1=1
count1=0
count2=0
print(value,index2,index3)
while True:
    if list1[index2]>value and count1==0:
        mul1*=index2
        count1+=1
    if list1[index2]>value and count1==0:
        index2-=1
    if list1[index3]>value and count2==0:
        mul1*=index3
        count2+=1
    if list1[index3]>value and count2==0:
        index3+=1
    if count1==1 and count2==1:
        break


print(mul1)
