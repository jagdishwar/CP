                list1=[1,4,2,3]
                list2=[2,5,1,6]
                combination=[]
                result=[]
                N=4
                N=N+1
                for i in list1:
                    for j in list2:
                        combination.append(i+j)

                def sortedheaps(list1):
                    n=len(list1)
                    for i in range(n,-1,-1):
                        heapify(list1,i,n)
                    for i in range(n-1,n-N,-1):
                        result.append(list1[0])
                        list1[i],list1[0]=list1[0],list1[i]

                        heapify(list1,index=0,end=i)


                def heapify(list1,index,end):
                    largest = index
                    lefti=index*2+1
                    righti=index*2+2
                    if lefti<end and list1[lefti]>list1[index]:
                        largest=lefti
                    if righti<end and list1[righti]>list1[largest]:
                        largest=righti
                    if largest!=index:
                        list1[largest],list1[index]=list1[index],list1[largest]
                        heapify(list1,largest,end)


                list1=combination
                sortedheaps(list1)
                print(result)