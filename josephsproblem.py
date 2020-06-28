list1=[2,3,4,5,6,46,8,9,10]
list2=[]
list4=[]
p=0
i=0
list5=[]
"""def oddinteger(list1):
    for i in range(len(list1)):
        if i%2!=0:
            return list1.remove(list1[i])"""



while len(list1)>3:
                for i in range(len(list1)):
                    if i%2!=0:
                        list5.append(list1[i])
                print(list5)
                for i in range(len(list5)-2,-1,-1):
                    list2.append(list5[i])
        
                for k in range(len(list5)-1,len(list5)-2,-1):
                    list2.append(list5[k])
        
                for l in range(len(list2)-1,-1,-1):
                    list4.append(list2[l])
        
        
                list1=list4

print(list1)


"""while i<len(list1):
    print(i)
    if i%2!=0:
        list1.remove(list1[i])
        print(list1)
    i+=1"""