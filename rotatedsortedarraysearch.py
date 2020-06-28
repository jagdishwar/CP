
list1=[ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
def findindex(s,e,list1):

    mid=(s+e)//2

    pivotindex=0
    if list1[mid]>list1[mid+1]:
        pivotindex=mid+1

    else:
        if list1[mid]<list1[s]:
            return findindex(s,mid-1,list1)

        else:
            return  findindex(mid+1,e,list1)
    return pivotindex


s=0
e=len(list1)-1
pivot=findindex(s,e,list1)

list2=[]
count=0
ele=202
if list1[pivot]<=ele<=list1[e]  :
    count+=1
    list2=list1[pivot:e+1]
else:
    list2=list1[s:pivot]
print(list2)
s=0
end=len(list2)-1




def binarysearch(s,end,list2,ele):

    while s<=end:

        mid = (s + end) // 2


        if list2[mid]==ele:
            return mid
        else:
            if ele<list2[mid]:
                end=mid-1
            else:
                s=mid+1

index=binarysearch(s,end,list2,ele)
if count==0:
    print(index)
else:
    print((len(list1)-len(list2)+index))

