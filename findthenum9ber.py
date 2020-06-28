def intersquareroot(k):
    low=0
    high=k
    while high>=low:
        mid=(high+low)//2
        middigit=mid*mid
        if middigit>=k:
            high=mid-1
        else:
            low=mid+1
    return low-1


print(intersquareroot(144))

