A=[ 96, 96, 7, 81, 2, 13 ]
list4=list(A)

list1=[]
def numberintobinary(num):

    if num>=1:
        numberintobinary(num//2)
    list1.append(num%2)
list2=[]
def numberintobinary1(num1):

    if num1>=1:
        numberintobinary1(num1//2)
    list2.append(num1%2)

def hammingdiatnce(list1,list2):
    count=0


    if len(list1)<len(list2):
        a=len(list1)
    else:
        a=len(list2)

    while a>=1:
        k=list1.pop()
        m=list2.pop()
        if k!=m:
            count+=1

        a-=1
    return count

list3=[]
for i in range(len(list4)):
    for j in range(len(list4)):

        numberintobinary(list4[i])
        numberintobinary1(list4[j])

        value = hammingdiatnce(list1, list2)
        list3.append(value)



print(sum(list3))
