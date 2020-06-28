def subset(list1,gotlist,sublist,index):

    gotlist.append(sublist[:])
    for i in range(index,len(list1)):
        if i>index and list1[i]==list1[i-1]:
            continue
        sublist.append(list1[i])
        subset(list1,gotlist,sublist,i+1)
        sublist.pop()

gotlist=[]
list1=[1,2,3]
subset(list1,gotlist,[],0)
print(gotlist)