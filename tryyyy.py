
import collections
a,b=map(int,input('ubdf').split())
list1=list(map(int,input('uybg').split()))

queue=collections.deque(list1)
for i in range(1,b):
    val1=list1[i-1]+list1[i]
    val2=list1[i-1]+list1[i+1]
    queue[i-1]=min(val1,val2)
    print(queue)





"""n=634
result=""
count=97
for i in range(n):
	result+=chr(count)
	if count>121:
		count=97
	else:
		count+=1
print(result)"""