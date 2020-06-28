list1=[-3,2,34,14,1,-2,3,64,-3,25,5,32]
i=0
j=len(list1)-1
while(1):
        while list1[i]<=0 and i<j:
            i+=1
        while list1[j]>=0 and i<j:
            j-=1
        if (i<j):
            list1[i],list1[j]=list1[j],list1[i]
            i+=1
            j-=1
        else:
            break

print(list1)