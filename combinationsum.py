def combinationsum(cadidates,index,target,sublist,list2):
    if target==0:
        list2.append(sublist[:])
        return
    elif target<0:
        return
    else:
        for i in range(index,len(cadidates)):
            sublist.append(cadidates[i])
            combinationsum(cadidates,i,target-cadidates[i],sublist,list2)
            sublist.pop()


list2=[]
iam=combinationsum([2,3,5],0,8,[],list2)
print(list2.sort())

"""list1=[2,3,6,7]
target=7
list2=[]
for i in range(len(list1)):
    rem=target % list1[i]
    flo = target // list1[i]
    if rem==0:
        list2.append([list1[i]]*flo)
    else:
        for j in range(len(list1)):
            if rem==list1[j]:
                list2.append(list1[i]*flo)
                list2.append(list1[j])

print(list2)



"""



