vowels = ['a', 'e', 'i', 'o', 'u']
n=len(vowels)

def dp(start, count):
    if count == n:
        return 1
    res = 0
    for i in range(start, len(vowels)):
        res = dp(i, count + 1) + res
    return res


print((dp(0, 0)))

