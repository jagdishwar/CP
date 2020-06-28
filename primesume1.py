A=1048574
prime = list(range(1, A + 1))
for i in range(2, len(prime)):
    if prime[i] == True:
        j = 2
        while j * i <= A:
            prime[j * i] = False
            j += 1

for i in range(2, A):
    if prime[i] and prime[A - i]:
        print(i, A - i)