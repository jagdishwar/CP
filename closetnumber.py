def closedinterger(list1,k):
    min_int=float("inf")
    low=0
    high=len(list1)-1
    closet=0
    while high>=low:
        mid=(low+high)//2

        if mid+1<len(list1):
            min_diff_left=abs((list1[mid+1])-k)

        if mid>0:
            min_diff_right=abs((list1[mid-1])-k)


        if min_diff_left<min_int:
            min_int=min_diff_left
            closet=list1[mid-1]
            print(closet)

        if min_diff_right<min_int:
            min_int=min_diff_right
            closet=list1[mid+1]
            print(closet)



        if list1[mid]<k:
            low=mid+1
        elif list1[mid]>k:
            high=mid-1

    return closet


list1=[1,4,5,6,7,8,9,11,23,45,75]
k=56
print(closedinterger(list1,k))







