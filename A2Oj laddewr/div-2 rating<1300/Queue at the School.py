n,t=map(int,input().split())
strx=list(input())
i=0
while i<n:
    if strx[i] == 'B':
        for j in range(i,t+i):
            if j+1<n:
                strx[j],strx[j+1]=strx[j+1],strx[j]
        i+=t
    i+=1
print(''.join(strx))

