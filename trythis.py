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
list4 = []
listre=[]
sum2 = 0
for i in range(len(list1)-1,-1,-1):
    listre.append(i)

print(list1)
for i in range(len(list1)):
    count = 0
    dict1 = {}
    divfact = 0
    list7 = []
    factormul = 1
    value=0


    for j in range(i+1 , len(list1)):
        if list1[i] > list1[j]:
            count += 1
    for p in range(i,len(list1)):
        if list1[p] in dict1 :
            dict1[list1[p]] += 1
        else :
            dict1[list1[p]] = 1


    list7 = list(dict1.values())


    for k in list7:
        re = factorial(k)
        factormul *= re

    po=listre[i]
    fatoria=factorial(po)



    value = ((count)*fatoria // factormul)



    sum2 += value

print(sum2+1% 1000003 % 1000003)
