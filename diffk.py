list1=[ 1,2,2,3,4]
lim=0
"""def dublicates(list1):
    count=0
    for i in list1:
        k=list1.count(i)
        print(k)
        if k>1:
            count=k
            return 1
    return 0
print(dublicates(list1))

if (k==0 and len(list1)==1) or (dublicates(list1)==1 and k==0):
                print(0,'fuvck yourself')

while j>i:
    if list1[j]-list1[i]==k:
        print(1)
    else:
        if list1[j]-list1[i]>k:
            j-=1
        else:
            i+=1

print(0)"""
for i in range(len(list1)):
    low=i+1
    high=len(list1)-1
    ele=list1[i]+lim
    print(ele,'ele')
    while low<=high:
        mid=(high+low)//2
        if list1[mid]==ele:
            print(1)
            break
        else:
            if ele<list1[mid]:
                high=mid-1
            else:
                low=mid+1
print(0)