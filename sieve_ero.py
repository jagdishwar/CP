
A=1048574
sieve = [True for i in range(1, A + 1)]
k = 2
while (k * k < A + 1):
    if sieve[k] == True:
        for i in range(k * k, A, k):
            sieve[i] = False
    k += 1

for i in range(2, A):
    if sieve[A - i] and sieve[i]:
        print(i, A - i)