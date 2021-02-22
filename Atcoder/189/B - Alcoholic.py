n,x=map(int,input().split())
count=0
flag=0
sum1 = 0
for _ in range(n):
    v,p=map(float,input().split())
    sum1+=int(v*p/100.000)
    count+=1
    if sum1>x:
        print(count)
        flag=1
        break
if flag==0:
    print(-1)



print(1.1+4)