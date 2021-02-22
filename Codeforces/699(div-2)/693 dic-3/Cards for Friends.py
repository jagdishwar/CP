t=int(input())
for _ in range(t):
    w,h,n=map(int,input().split())
    count=0
    def iseven(x):
        if x%2==0:
            return True
        return False
    while iseven(w) or iseven(h):
        if iseven(w) :
            w=w/2
        elif iseven(h):
            h=h/2
        count+=1
    if 2**count>=n:
        print('YES')
    else:
        print('NO')
