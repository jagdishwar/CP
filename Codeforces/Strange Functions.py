
def fx(n):
    num=0
    while n:
        c = n % 10
        num = (num * 10 + c)
        n = n // 10
    return num
def gx(x):
    return x/fx(fx(x))

for _ in range(6):
    n=int(input())
    sett={1}
    for x in range(0,n+1,10):
        val=gx(x)
        if val:
            sett.add(val)

    print(len(sett))






