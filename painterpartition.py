list1=[10,20,30,40]
l=max(list1)
h=sum(list1)
enter=4
while h>=l:
    mid=h+l//2
    if list1[mid]==enter:
        print(mid)
    else:
        if list1[mid]<=enter:
            h=mid-1
        else:
            l=mid+1

