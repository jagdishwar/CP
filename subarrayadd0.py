list1=[1,2,-5,1,2,-1]
i=0
add=0
list3=[]
while i<len(list1):
    while not list1[i]<0:
        i+=1
    k=i
    l=i
    list2=[]
    right=0
    left=0
    right=k+1
    left=l-1
    print(i)
    print("right",right)
    print("left",left)
    while right<len(list1) and left>=0 and not add<0:
        add+=list1[right]
        print(list1[right],"list1right")
        list2.append(list1[right])
        if add==0:
            print("afae")
            break
        add+=list1[left]
        list2.append(list1[left])


        if add == 0:
            print("afae")
            break
        right += 1
        left-=1
    if sum(list2)==0:
        list3=list2
        break
print(list3)


