import numpy as np
list2= [   [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]   ]
list1=np.array(list2).reshape(1,9)
print(list1)

s=0
end=len(list2)-1




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



                new_list=[]
                for i in range(len(list2)):
                        new_list.extend(list2[i])

                new_list.sort()
                print(new_list[len(new_list)//2])

