        list1=[1,2,3,4]
        left_list=[1]*len(list1)
        right_list=[1]*len(list1)
        output=[]
        for i in range(1,len(list1)):
            left_list[i]=list1[i-1]*left_list[i-1]
        for i in range(len(list1)-2,-1,-1):
            right_list[i]=list1[i+1]*right_list[i+1]


        for i in range(len(list1)):
            output.append(left_list[i]*right_list[i])

        print(output)