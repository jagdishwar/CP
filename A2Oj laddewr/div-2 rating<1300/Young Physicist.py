t=int(input())
dx=0
dy=0
dz=0
for i in range(t):
    x,y,z=map(int,input().split())
    dx+=x
    dy+=y
    dz+=z

if dz==0 and dx==0 and dz==0:
    print('YES')
else:
    print('NO')