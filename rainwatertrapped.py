list1=[0,1,0,2,1,0,1,3,2,1,2,1]
l=0
r=len(list1)-1
left_max=0
right_max=0
result=0
while r>l:
    if list1[l]>list1[r]:
        if right_max<list1[r]:
            right_max=list1[r]
        else:
            result+=right_max-list1[r]
        r-=1
    else:
        if left_max<list1[l]:
            left_max=list1[l]
        else:
            result+=left_max-list1[l]
        l+=1
print(result)

















"""list1=[0,1,0,2,1,0,1,3,2,1,2,1]
            maxx=max(list1)
            list2=[]
            for j in range(len(list1)-1,-1,-1):
                if list1[j]==maxx:
                    list2 = list1[j + 1:]
                    list1=list1[:j+1]


                    break
            print(list1)
            print(list2)
            if list1[0]==0:
                list1=list1[1:]
            queue=[]
            store=[]
            def findingwater(list1,queue,store):
                    for i in range(len(list1)):

                        count=0
                        while queue and list1[queue[0]]<=list1[i]:
                            if count==0:
                                queue.append(i)
                                count=1
                            index1=queue.pop()
                            last=list1[index1]
                            if queue:
                                k=list1[queue[-1]]
                                k2=list1[queue[1]]
                                first=list1[queue[0]]
                                index2=queue[0]
                                del queue[0]
                                ele1=last-k
                                ele2=first-k2
                                char1=min(ele1,ele2)
                                store.append(char1*(index1-index2-1))

                        queue.append(i)
            findingwater(list1,queue,store)
            k=sum(store)
            queue=[]
            store=[]
            findingwater(list2,queue,store)
            l=sum(store)
            print(k+l)"""