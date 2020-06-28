list1= ['0.6', '0.7', '0.8', '1.2', '0.4']
list2=[]

for i in list1:
    list2.append(float(i))

print(list2)
list2.sort()
for k in list2:
    ele=k
    start=list2.index(k)+1
    end=len(list2)-1
    if ele<2:
        while start<end:
            if 1<ele+list2[start]+list2[end]<2:
                print(1)
                break
            if  ele+list2[start]+list2[end]>2:
                end-=1
            if ele+list2[start]+list2[end]<1:
                start+=1




print(-1)