n,k=map(int,input().split())
def revfun(num):
    val=0
    list1=[]
    while num:
        val=num%10
        list1.append(val)
        num=num//10
    list1.sort()
    return list1

def listtonum(list1):
    num=0
    for i in list1:
        num=num*10+i
    return num

for i in range(k):
    list1=revfun(n)
    list1.sort()
    num1=listtonum(list1)
    num2=listtonum(list1[::-1])
    n=num2-num1
    if k==0:
        break

print(n)