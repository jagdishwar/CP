list1= [ 4, 0, 2, 1, 3 ]
max1=max(list1)+1

mini=0
maxi=len(list1)-1
for i in range(len(list1)):
        if i%2==0:
            list1[i]=list1[i]+list1[maxi]%len(list1)*len(list1)
            maxi-=1
        else:
            list1[i]=list1[i]+list1[mini]%len(list1)*len(list1)
            mini+=1





for i in range(len(list1)):
    list1[i]=list1[i]//max1

print(list1)
