strx = "aabaa"
low = 0
high = len(strx) - 1
count = 0
if len(strx) == 1:
    print(0)
while low <= high:
    print(low, high,'low,hihg')
    if strx[low] == strx[high] and high != low:
        count+= 2
        high -= 1

    if high == low:
        count+= 1
    print(count,'count')
   else:
    low += 1
print(count)
print(len(strx) - count)