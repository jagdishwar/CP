arr=[2,3,5]
n=len(arr)
ans=0
num=999
for mask in range(1,1<<n):
    toggle=mask
    temp=1
    pos=0
    bits=0
    while mask:
        lastbit=mask&1
        if lastbit:
            temp*=arr[pos]
            bits+=1
        mask>>=1
        pos+=1
    if bits&1:
        ans+=num//temp
    else:
        ans-=num//temp

print(ans)


