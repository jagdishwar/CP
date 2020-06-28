
A = [1,5,8]
B = [6,9]

i = 0
j = 0
while i < len(A) and j < len(B):
    if A[i] > B[j]:
        print(i)
        print(B[j])
        A.insert(i, B[j])
        j += 1
    else:
        i += 1
while j < len(B):
    A.append(B[j])
    j += 1

print(A)
