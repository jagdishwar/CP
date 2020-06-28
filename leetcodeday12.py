import heapq
list1=[3,7,2]
list1=[-x for x in list1]
heapq.heapify(list1)
while len(list1)>1:
    print(list1)
    maxele=heapq.heappop(list1)
    maxele2=heapq.heappop(list1)
    diff=maxele-maxele2
    print(diff)
    heapq.heappush(list1,diff)


print(list1)