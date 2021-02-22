from itertools import permutations


t=int(input())
for _ in range(t):
    n=int(input())
    list1=[]
    str1=input()
    str2=input()

    for i in range(n):
        list1.append([str1[i],str2[i]])

    count1=0
    count2=0
    result=[]

    result=list(permutations(list1))

    for i in result:
        int1=""
        int2=""
        for j in i:
            int1+=j[0]
            int2+=j[1]
        if int(int1)>int(int2):
            count1+=1
        elif int(int2)>int(int1):
            count2+=2

    if count1>count2:
        print('RED')
    elif count1<count2:
        print('BLUE')
    elif count1==count2:
        print('EQUAL')

