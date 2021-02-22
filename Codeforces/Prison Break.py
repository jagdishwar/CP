N=int(input())
for _ in range(N):
    n,m,r,c=map(int,input().split())
    print(max(abs(1-r)+abs(1-c),abs(1-r)+abs(m-c),abs(n-r)+abs(1-c),abs(r-n)+abs(c-m)))





[3,2,1,1,3,3,5,7,8,9]