t=int(input())

for _ in range(t):
    n, k, s = map(int, input().split())
    g=n//k
    if s<7 and n>k:
        print("1")
    elif s>7 and n>k:
        if s-g<7:
             print("2")
        else:
            f=s//g
            print(f+1)
    elif s==7 and g*s>=n:
        print("1")
    elif s>=7 and g*s<=n:
        print("-1")

    else:
        print("-1")

