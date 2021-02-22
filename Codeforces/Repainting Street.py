from collections import defaultdict

N=int(input())
for _ in range(N):
    n,k=map(int,input().split())
    list1=map(int,input().split())
    dict1 = {}
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1



    print(dict1)
    val=0
    keyy=0
    for key,value in dict1.items():
        if val<value:
            keyy=key
            val=value
    count=0
    print(keyy)
    for i in range(n):
        print(list1[i])
        if list1[i]!=keyy:
            for j in range(k):
                list1[i+j]=keyy
            count+=1
    print(count)









