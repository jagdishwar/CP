def insertheaps(list1,n,value):
     n=n+1
     list1[n]=value
     while i>1:
         parent=i//2
         if list1[parent]<list1[i]:
             list1[parent],list1[i]=list1[i],list1[parent]
             i=parent

         else:
             return True


def heapifyofheaps(list1,n,i):
    largest=i
    left=i*2
    right=i*2+1
    while left<=n and list1[largest]<=list1[left]:
        largest=left
    while right<=n and list1[largest]<=list1[right]:
        largest=right
    if largest!=i:
        list1[largest],list1[i]=list1[i],list1[largest]
        heapifyofheaps(list1,n,largest)



