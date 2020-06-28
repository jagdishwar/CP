            list1=[1,2,4]
            list2=[]
            str1=""
            for i in list1:
                str1+=str(i)

            str1=int(str1)+1
            str1=str(str1)
            for i in str1:
                list2.append(i)
            print(list2)