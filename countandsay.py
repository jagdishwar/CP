def saystring(list1):
    i=0
    result=[]
    while i<=len(list1)-1:
        count=1
        while (i+1)<=len(list1)-1 and list1[i+1]==list1[i]:
            count+=1
            i+=1
        result.append(str(count)+list1[i])
        i+=1
    return ''.join(result)

n=5
list1='1'

for i in range(n-1):
    list1=saystring(list1)
return list1