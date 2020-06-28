str1=str(3245)
count=1
list1=[]
i=0
l=0
while count<len(str1):
    countdown=0
    k=""
    while i<len(list1):
        l=i
        j=list1[l]
        if countdown<count:
            k+=j
            countdown+=1
            l+=1
        if countdown==count:
            list1.append(k)
            k=""
            i+=1
            l=i
            countdown=0

    count+=1

print(list1)