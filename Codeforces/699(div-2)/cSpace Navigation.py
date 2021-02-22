t=int(input())
for _ in range(t):
    px,py=map(int,input().split())
    dx =px
    dy =py
    strx=input()
    flag=0
    for i in strx:
        if i=='U' and py-dy+1<=py:
            dy-=1
        if i=='D' and py-dy-1>=py:
            dy+=1
        if i=='R' and  px-dx+1<=px  :
            dx-=1
        if i=='L' and px-dx-1>=px:
            dx+=1

        if dx==0 and dy==0:
            print('YES')
            flag=1
            break
    if flag==0:
        print('NO')


