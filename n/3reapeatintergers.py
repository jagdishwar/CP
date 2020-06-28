list1=list(A)
        set1=set(list1)
        list2=list(set1)
        for i in list2:
            count1=list1.count(i)
            if count1>(len(list1)//3):
                return i
        return -1
also a solution