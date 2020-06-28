list1=[ 31, 14, 19, 75 ]
std=12
l=max(list1)
h=sum(list1)
def minvalue(list1,std,mid):
    k=std
    minvalue=mid
    nostd=1
    total=0
    for i in list1:
        total+=i
        if total>minvalue:
            total=i
            nostd+=1

    return nostd



while h>l:
    mid=l+(h-l)/2
    noofstd=minvalue(list1,std,mid)
    if noofstd<=std:
        h=mid
    else:
        l=mid+1
print(int(l))


