'''
Lucas Theorem :
Lucas' theorem is a result about binomial coefficients modulo a prime p.
We will be given three numbers n, r and p and we need to compute value of nCr mod p.
Excample 1:
Q.) : Find the remainder when 1000C300 is divided by 13.
Sol : First we write 1000 and 300 in terms of the sum of power of 13
             1000 = 5(13^2) + 11(13) + 12
              300 = 1(13^2) + 10(13) + 1
        Then apply Lucas Theorem:
                                1000C300 = (5C1) * (11C10) * (12C1)
                                         = 5 * 11 * 12
                                         = 5 *(-2) * (-1)
                                         = 10


'''
from scipy.special import comb
def base(x,n):
    while x:
        yield x%n
        x//=n


def lucas(n,k,MOD):
    result=1
    for nn,kk in zip( base(n,MOD),base(k,MOD)):
        result*=comb(nn,kk,exact=True)
    return result%MOD

print(lucas(10,2,13))

