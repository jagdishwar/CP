list1=[ 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0 ]
M=4
jump=M+1
countmax=0
countzero=0
list2=[]
i=0
j=0
while i<=len(list1)-1 and j<=len(list1)-1:
    if list1[j] is 1 and jump>=0:
        jump=M

    if list1[j] is 0:
        jump-=1
    if list1[j] is 1 and jump<0:
        i=j
        countmax=0
    list2.append(j - i)
    j+=1


print(list2)


