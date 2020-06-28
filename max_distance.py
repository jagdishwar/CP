list1=[10,1,6,3,9,0]
list2=[]
for i in list1:
    list2.append(i)
list1.sort()
list3=[]
for i in range(len(list1)):
       list3.append(list1.index(list2[i]))
max_index=list3[-1]
ans=int(None)
for i in range(len(list3)-1,-1,-1):
    if max_index-list3[i]>ans:
        ans=max_index-list1[i]
        print(ans)
    max_index=max(list3[i],max_index)

print(ans)





