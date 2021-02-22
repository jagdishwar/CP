import collections
prices=[3,6,9,8,2,4]
mn=float('inf')
dict1=collections.defaultdict(list)
profit=[5,0,2]
for k in profit:
    dict1[k].append([])
list1=[[0] for i in range(len(profit))]
print(dict1)

for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        if prices[j]-prices[i] in dict1:
            dict1[prices[j]-prices[i]].append([i+1,j+1])

list1=[]
for key,value in dict1.items():
    temp=[]
    for val in value:
        if val!=[]:
            temp.append(val)

    list1.append(temp)
print(list1)
for ond in list1:
    ond.sort(key=lambda x:(x[1],x[1]-x[0]))
resultlist=[]
print(list1)
for i in range(len(profit)):

    if list1[i]==[]:
        resultlist.append([-1])
    else:
        resultlist.append(list1[i][0])

result=""
for val in resultlist:
    for k in val:
        if k!=val[-1]:
            result+=str(k)+' '
        else:
            result+=str(k)+','


print(result[:-1])







"""result=""
print(dict1)
for key,value in dict1.items():
    if key !=[]:
            print(value[-1][-1],'df')
            for k in value[0]:
                print(k)
                result+=str(k)+' '
    else:
            result+='-1'


    result+=','

print(result[:-2])
"""