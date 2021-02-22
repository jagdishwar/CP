from collections import defaultdict
t=int(input())
for _ in range(t):
    n = int(input())
    list1=list(map(int,input().split()))
    poslist=[abs(i) for i in list1]
    maxele=max(poslist)
    index=poslist.index(maxele)

    dictsub=defaultdict(int)
    print(list1)
    for i in range(n):
        for j in range(n):
            if i!=j:
                dictsub[list1[i]]+=abs(list1[j]-list1[i])
    print(dictsub)
    dict1=sorted(dictsub.items(),key=lambda x:x[1])
    ele=dict1[0][0]
    print(dict1)
    list1[index]=dict1[0][0]
    count=0
    i=0
    while [ele]*n!=list1:
            j=list1[i]
            k=list1[i]
            prev=float('inf')
            while list1[j]!=ele and prev>list1[j]:
                list1[j]-=1
                prev=list1[j]
                count+=1
            prev=-float('inf')
            while list1[k]!=ele and prev<list1[k]:
                list1[k]+=1
                prev=list1[k]
                count+=1
    print(count)










