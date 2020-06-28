"""
   [a, b, r]
   abadracadabra
   3
 """
minvalue = float('inf')
res = ""
for i in range(len(str)):
    counter = 0
    seen = set()
    for j in range(i, len(str)):
        if str[j] not in arr:
            continue
        if str[j] not in seen:
            counter += 1
        seen.add(str[j])
        if counter == len(arr) and (j - i + 1) < minvalue:
            res = str[i:j + 1]
            minvalue = len(res)
            if minvalue == len(arr):
                return res
            break
return res

for i,item in enumerate(list1):

arr = ['x', 'y', 'z']
str = "xyyzyzyx"