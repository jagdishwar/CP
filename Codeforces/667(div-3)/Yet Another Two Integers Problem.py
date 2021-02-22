t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    x=1
    z=max(a,b)
    count1=0
    count2=0
    while not 1*x<=z<=10*x:
        x*=10
        count1+=1
    y=1
    m=min(a,b)
    while not 1*y<=m<=10*y:
        y*=10
        count2+=1
    print(a,b,count1,count2)
    if count1==count2:
        if a==b:
            print(0)
        else:
            print(round(z/m))
    else:
        val=abs(count1-count2)
        a=a/(10**val)
        b=b/(10**val)
        print(round(abs(a-b)))

