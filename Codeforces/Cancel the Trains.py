t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    set1=set()
    count=0
    for i in list1:
        set1.add(i)
    for i in list2:
        if i in set1:
            count+=1

    print(count)