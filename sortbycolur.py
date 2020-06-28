            list1=[0,1,2,0,1,2]
            dict1={}
            for i in range(len(list1)):
                if list1[i] in dict1:
                    dict1[list1[i]]+=1
                else:
                    dict1[list1[i]]=1
            del list1[:]

            for key,value in dict1.items():
                list1.extend([key]*value)
            print(list1)