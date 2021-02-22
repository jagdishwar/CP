def multi(f,m):
    mod = 1000000007

    a = (f[0][0] * m[0][0] % mod + f[0][1] * m[1][0] % mod) % mod
    b = (f[0][0] * m[0][1] % mod + f[0][1] * m[1][1] % mod) % mod
    c = (f[1][0] * m[0][0] % mod + f[1][1] * m[1][0] % mod) % mod
    d = (f[1][0] * m[0][1] % mod + f[1][1] * m[1][1] % mod) % mod
    f[0][0] = a
    f[0][1] = b
    f[1][0] = c
    f[1][1] = d


I=[[1,0],[0,1]]
A=[[1,1],[1,0]]
def power(F, n):

    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]

    power(F, n // 2)
    multi(F, F)


    if n&1:
        multi(F, M)



power(A,8-1)
print(A[0][0])