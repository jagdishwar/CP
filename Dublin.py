import math

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

dv=[]
for _ in range(int(math.log2(K))+1):
    l=[0]*N
    dv.append(l)


for i in range(N):
    dv[0][i]=A[i]-1

for k in range(1, int(math.log2(K))+1):
    for i in range(N):
        dv[k][i]=dv[k-1][dv[k-1][i]]

a=[]
for i in range(int(math.log2(K)) + 1):
    if K>>i &1:
        a.append(i)
