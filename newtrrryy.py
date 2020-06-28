A=[1,3,5,34,23,45]
B=1
i = 0
j = 0
while (j < len(A)):
    if (A[j] != B):
        A[i] = A[j]
        i += 1
    j += 1


print(i)
