import heapq
arr=[10,7,5,20]
K=3
eaten = 0
listx = arr
list1 = [-x for x in listx]
heapq.heapify(list1)
sum1=0
for i in range(K):
    ele = heapq.heappop(list1)*-1
    heapq.heappush(list1,-(ele//2))

for i in list1:
    sum1+=-i
print(sum1)
"""

def dp(i,K):
    if K<=0:
        return 0
    if i>=len(arr)-1:
        return 0


    ans=float('inf')

    ans=min((dp(i,K-1)+abs(arr[i])//2),dp(i+1,K)+abs(arr[i+1]))
    

    return ans

print(dp(0,K))
"""