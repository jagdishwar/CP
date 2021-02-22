x=input()
m=int(input())
import math
def greatnum(num):
    val=0
    maxvalue=-float('inf')
    while num:
        val=num%10
        maxvalue=max(maxvalue,val)
        num=num//10
    return maxvalue

count=0
def int2base(num,base):
    sum1=[]
    result=[]
    for i in range(1,1000):
        if base**i>=num:
            break
    for j in range(i):
        sum1.append(base**j)
    print(sum1)
    for val in sum1[::-1]:
        print(num)
        result.append(str(num // val))
        num=abs(math.remainder(num,val))



    val=''.join(result)
    return val

for i in range(greatnum(int(x))+1,m):

    if i==37:
        break
    if int(x,i)<m :
        count+=1


print(int2base(120760, 60))