t=int(input())
for _ in range(t):
    list1=list(map(int,input().split()))
    maxvalue=max(list1)
    minvalue=min(list1)
    a,b,c=0,0,0
    if list1.count(maxvalue)>1:
        print('YES')
        a=maxvalue
        b=minvalue
        if minvalue==1:
            c=1
        else:
            minvalue-=1
            c=minvalue
        print(a,b,c)

    else:
        print('NO')







