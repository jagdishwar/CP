t=int(input())
for _ in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    count1=0
    count2=0
    for i in list1:
        if i==1:
            count1+=1
        elif i==2:
            count2+=1

    if count1%2!=0:
        print('NO')
    elif count2%2!=0:
        if count1>0 and count1%2==0:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')