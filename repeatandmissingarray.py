A=[3, 1 ,2 ,5 ,3]
seen = set()
len_a = len(A)
sum_a = (len_a * (len_a + 1)) // 2
print(sum_a)
repeated = None

for i in A:
    if i not in seen:
        seen.add(i)
        sum_a -= i
    else:
        repeated = i
print(repeated, sum_a)