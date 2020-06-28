
def checkBitSet(bitNo,number):
    mask=1<<bitNo
    print('mask',bin(mask)[2:])
    print('number',bin(number)[2:])
    result=number&mask
    print(result,'result')
    if result!=0:
        return True
    else:
        return False
A=[1, 3, 5]
answer = 0
n = len(A)
MOD = 10 ** 9 + 7
for i in range(31, -1, -1):
    count = 0
    for j in A:
        if checkBitSet(i, j):
            count += 1
    print(count,'count')
    answer += count * (n - count) * 2
    print(answer,'answer')
print(answer % MOD)
