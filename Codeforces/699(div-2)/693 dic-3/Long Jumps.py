from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    maxvalue=-float('inf')
    dict1=dict()

    for i in range(len(list1)):
        val=0
        j=i
        while j < len(list1):
               val += list1[j]
               j+=list1[j]
        if val>maxvalue:
            maxvalue=val

    print(maxvalue)
st = time.time()
print("----%.2f----"% (time.time()-st))




