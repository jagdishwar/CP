import heapq
eaten=0
K=3
listx=[6,5]
list1=[-x for x in listx]
heapq.heapify(list1)
for i in range(K):
        heapq.heapify(list1)
        ele=heapq.heappop(list1)*-1
        eaten+=ele
        heapq.heappush(list1,-(ele//2))
        print(list1)

print(eaten%(10**9+7))