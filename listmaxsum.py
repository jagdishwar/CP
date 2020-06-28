list1 = [1, 2, 5, -7, 2, 3]
max_value = 0
array_add = 0
list2 = []
for i in range(len(list1)):
    array_add += list1[i]
    if max_value < array_add:
        max_value = array_add

        list2.append(list1[i])
        index1 = list1.index(list2[0])


        if len(list2)>1:
            last_ele=list2.pop()


            index2 = list1.index(last_ele)


            del list2[0:len(list2)]

            for i in range(index1,index2+1):
                list2.append(list1[i])




    if array_add < 0:
        array_add = 0
        for i in list2:
            list2.remove(i)

print(list2)