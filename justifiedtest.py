list1=["This", "is", "an", "example", "of", "text", "justification."]
limit=16//len(list1)
list2=[]
count=0
i=0
while True:
        str1=''
        count=0
        while count<=16:
            length=len(list1[i])
            i+=1
            count+=length+1
            print(count)
            str1+=list1[i]+' '
            if count>=16:
                break
        list2.append(str1)



print(list2)
list3=[""]
print(len(list3))