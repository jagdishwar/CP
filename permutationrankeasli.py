def factorial(num1):
    if num1 is 1:
        return 1
    if num1 == 0:
        return 0
    else:
        return num1 * factorial(num1 - 1)


list1 = []
str2 = A
for i in str2:
    list1.append(ord(i))

list2 = []
list3 = []
for i in range(len(list1)):
    count = 0
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            count += 1


    list2.append(count)
for i in range(len(list1)):


for j in range(len(list1)):
    list3.append(factorial(j))

list3.reverse()

sum1 = 0
for i in range(len(list1)):
    sum1 += list2[i] * list3[i]
print(sum1 + 1 % 1000003)