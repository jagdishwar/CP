t=int(input())
for i in range(t):
        n=int(input())
        list1=[]
        list2=[]
        list3=[]
        for i in range(n):
            list2=list(map(int,input().split(' ')))

            list1.append(list2)

        for i in range(len(list1)):

                if list1[i][0]<=8:
                    list3.append(list1[i])
        sum3=0
        value=0
        dict1={}
        for i in range(len(list3)):
            if list3[i][0] not in dict1:
                dict1[list3[i][0]]=list3[i][1]
            if list3[i][0] in dict1:
                k=dict1.get(list3[i][0])
                if k<list3[i][1]:
                    dict1[list3[i][0]]=list3[i][1]
        values=list(dict1.values())
        print(sum(values))

