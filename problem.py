        list1=[1,3,-1]
        maxvalue=0
        for i in range(1,len(list1)+1):
            for j in range(i+1,len(list1)+1):
                maxvalu=(abs(list1[i-1]-list1[j-1])+abs(i-j))
                if maxvalu>maxvalue:
                    maxvalue=maxvalu
        print(maxvalue)

