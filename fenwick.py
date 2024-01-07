n,m=map(int,input().split())
array=[int(i) for i in input().split()]

n=len(array)
bit = [0 for i in range(n + 1)]

def update_value(index, value):
    if 0<=index<n:
        index+=1

    while index <= n:
        bit[index-1] += value
        index += index & -index


def get_uptosum(index):
    summ = 0
    while index > 0:
        summ+= bit[index-1]
        index -= index & -index

    return summ

for i in range(n):

    update_value(i,array[i])


for _ in range(m):
    t,u,v=map(int,input().split())
    if t==0:
        update_value(u,v)
    else:
        x=get_uptosum(u)
        y=get_uptosum(v)
        print(y-x)



