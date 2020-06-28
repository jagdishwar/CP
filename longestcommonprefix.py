list1 = [ "abcd", "abde", "abc" ]

inrcc=0
count=0
print(min(list1))
for j in range(len(list1[0])):
    if count == 1:
        break
    for i in range(1,len(list1)):
        print(list1[0][j],'list1=--090')
        print(list1[i][j],'gibe 111')
        if list1[0][j]==list1[i][j]:
            inrcc+=1
        else:
            count=1
            break
doit=len(list1)-1

meas=inrcc//doit
print(list1[0][:meas],'fef')



