list1=[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
straight_dict={}
maximum=0
for i in range(len(list1)):
    straight_dict={}
    same=1
    for j in range(i+1,len(list1)):
        if list1[i][0]==list1[j][0] and list1[i][1]==list1[j][1]:
            same+=1
        elif abs(list1[j][0]-list1[i][0])==0:
            store='inf'
            if store in straight_dict:
                straight_dict[store] += 1
            else:
                straight_dict[store] = 1

        else:
          store=(list1[j][1]-list1[i][1])/(list1[j][0]-list1[i][0])
          if store in straight_dict:
              straight_dict[store] += 1
          else:
              straight_dict[store] = 1


    localmax=0
    for key,value in straight_dict.items():
        localmax=max(localmax,value)
    localmax+=same
    maximum=max(maximum,localmax)


print(maximum)