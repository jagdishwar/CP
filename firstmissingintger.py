
A=[1,2,3,1,1]
n = len(A)
l = n / 3

maj1 = 0
maj2 = 0
first = float('inf')
second = float('inf')

for i in range(n):
    print('iiiiiii',i)
    print('valieuer',A[i])
    print('maj1111',maj1)
    print('maj22222',maj2)
    print('             ')
    if first == A[i]:
        maj1 += 1
        print('maj1',maj1)
    elif second == A[i]:
        maj2 += 1
        print('maj2',maj2)
    elif maj1 == 0:
        print('fuck you')
        maj1 += 1
        first = A[i]
        print(first,'first')
    elif maj2 == 0:
        print('fuck you 1')
        maj2 += 1
        second = A[i]
        print('second',second)
    else:
        maj1 -= 1
        maj2 -= 1

maj1 = 0
maj2 = 0
print(first)
print(second,'wee')

for i in range(n):
    if A[i] == first:
        maj1 += 1
    elif A[i] == second:
        maj2 += 1

if (maj1 > l):
    print(first,'first')

if (maj2 > l):
    print(second,'second')
