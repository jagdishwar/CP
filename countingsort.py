list1=[3,4,3,0,2,4,2,9,2,3,4,9,1,9]
countlist1=[0 for i in range(max(list1)+1)]
blist1=[0 for p in range(len(list1))]
def countingsort(list1, countlist):
    for i in range(len(list1)):
        countlist1[list1[i]]+=1
    for j in range(1,len(countlist1)):
        countlist1[j]=countlist1[j]+countlist1[j-1]
    for g in range(len(list1)-1,-1,-1):
        countlist[list1[g]]-=1
        k=countlist1[list1[g]]
        blist1[k]=(list1[g])#decrement position in count list store  the list element
countingsort(list1,countlist1)

print(blist1)