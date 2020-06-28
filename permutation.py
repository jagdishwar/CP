def factorial(num1):
    if num1 is 1:
        return 1
    if num1==0:
        return 0
    else:
        return num1*factorial(num1-1)



list1=[]
str2='DTNGJPURFHYEW'
str2.lower()
for i in str2:
    list1.append(ord(i))
print(list1)
list2=[]
list3=[]
for i in range(len(list1)):
    count=0
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            count+=1
    list2.append(count)
for j in range(len(list1)):
    list3.append(factorial(j))
print(list2)
list3.reverse()
print(list3)
sum1=0
for i in range(len(list1)):
    sum1+=list2[i]*list3[i]
print(sum1+1)
# if list2[i]==list1[j] and list2[i]!=0:
##    sum1+=1
#   level+=1
# elif list1[j]!=list2[i]:
#   sum1 += factorial(int(len(list2)-level

