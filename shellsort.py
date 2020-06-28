def shellsort(list1):
    gap=len(list1)//2
    while gap>0:
        for index in range(gap,len(list1)):
            current_value=list1[index]
            pos=index
            while pos>=gap and current_value<list1[pos-gap]:
                list1[index]=list1[index-gap]
                pos=pos-gap
            list1[pos]=current_value
        gap=gap//2





list1=[3,34,352,23,4,1,34674,5,345,234,35]
print(shellsort(list1))
print(list1)
