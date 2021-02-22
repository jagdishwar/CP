import functools
from collections import deque
def ignore_unhashable(func):
    uncached = func.__wrapped__
    attributes = functools.WRAPPER_ASSIGNMENTS + ('cache_info', 'cache_clear')
    @functools.wraps(func, assigned=attributes)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError as error:
            if 'unhashable type' in str(error):
                return uncached(*args, **kwargs)
            raise
    wrapper.__uncached__ = uncached
    return wrapper

@ignore_unhashable
@functools.lru_cache()
def dp(stocks,costs,profit,counts,results):
   maxindex = len(profit)-1
   valmax = costs[maxindex]
   print(valmax)
   for i in range(int(stocks[1])):
       if stocks[2] > counts and stocks[2]>=counts + valmax:
           counts = counts + valmax
           results = results + ((valmax * profit[maxindex]) / 100)
       else:
           lastresult[0]+=results
           return results
   profit.pop(maxindex)
   costs.pop(maxindex)
   dp(stocks,costs,profit,counts,results)

stocks = list(map(int,input().split()))
costs = list(map(float,input().split()))
profit = list(map(float,input().split()))
list1=[]
for i in range(len(costs)):
    list1.append([profit[i],costs[i]])

list1.sort(key=lambda x:x[0])
print(list1)
counts = 0
results= 0

lastresult=[0]
val = dp(stocks,costs,profit,counts,results)

print(int(lastresult[0]))
"""4 2 100
20 10 30 40
5 10 30 20
"""