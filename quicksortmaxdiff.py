list1=[1,10,5]
def quicksort(list1,first,last):
    pivot=list1[last]
    left=first
    right=last-1
    while True:
        if left<=right and list1[left]<=pivot:
            left+=1
        if left<=right and list1[right]>=pivot:
            right-=1
        if right<left:
            list1[left],list1[last]=list1[last],list1[left]
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]

    return left
def quick_sort_recurrsion(list1,first,last):

    if first<last:
            pin = quicksort(list1, first, last)
            quick_sort_recurrsion(list1,first,pin-1)
            quick_sort_recurrsion(list1,pin+1,last)

quick_sort_recurrsion(list1,0,len(list1)-1)

print(minvalue)
