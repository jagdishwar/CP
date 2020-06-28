        n=4
        k=2
        list2=[]
        for i in range(1,n+1):

            for j in range(i+1,n+1):
                if j!=i:
                    list2.append([i,j])

        print(list2)