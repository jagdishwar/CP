list2=output
s=0
end=len(list2)-1
ele=10



def binarysearch(s,end,list2,ele):

    while s<=end:

        mid = (s + end) // 2


        if list2[mid]==ele:
            return mid
        else:
            if ele < list2[mid]:
                end=mid-1
            else:
                s=mid+1

index=binarysearch(s,end,list2,ele)
indexx=index
lowe=0
upp=0




while True:

    if ele==list2[indexx] and indexx>=0:
        indexx=indexx-1
        lowe=indexx
    else:
        break

while True:

    if ele==list2[index] and index<=len(list2)-1:
        index=index+1
        upp=index
    else:
        break
print(lowe+1,upp)

