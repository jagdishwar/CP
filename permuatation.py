            list1=[ 251, 844, 767, 778, 658, 337, 10, 252, 632, 262, 707, 506, 701, 475, 410, 696, 631, 903, 516, 149, 344, 101, 42, 891, 991 ]
            list2=[]
            for i in list1:
                list2.append(i)

            list2.sort()
            listrev=[]
            for i in range(len(list2)-1,-1,-1):
                listrev.append(list2[i])

            if listrev==list1:
                    print(list2)

            if list2==list1:
                    list1[-1],list1[-2]=list1[-2],list1[-1]
                    print(list1)
            if list2!=list1:
                    for i in range(len(list1)):
                        if list2[i]!=list1[i]:
                            list2[i],list2[i-1]=list1[i-1],list1[i]
                            print(list2)
