list1=  [ -6, -1, 4 ]
list2=[x for x in range(len(list1))]

for i in list2:
    count = 0
    flag=0
    for j in range(len(list1)):
        if list1[i]==list1[j] and list1[i]==0 :
            flag+=1
            continue

        if (list1[i]==list1[j] and flag>=1) or (list1[i]!=list1[j]):
                if list1[i]>=0:
                     if list1[j]>=list1[i]:
                            count+=1
                else:
                     print('list1111',list1[i],list1[i])

                     if list1[i]<=list1[j]:
                            count+= 1
                            print(count)





    if count==abs(list1[i]):
        print(1)
        break

print(-1)

