##find nCr%MOD

from math import factorial

# List of primes up to 50
_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def factors(M):
    """
    Return prime factors of M
    Ignore multiplicity since M is given as squarefree
    """
    return [p for p in _primes if M % p == 0]


def digits(n, p):
    """
    Return the digits of n written in base p
    """
    while n:
        yield n % p
        n //= p


def inverse(n, p):
    """
    Use eulers theorem to find the inverse of n mod p
    p is assumed to be prime
    """
    return pow(n, p - 2, p)


def choose(n, k):
    """
    Calculate n choose k
    """
    if n == k == 0:
        return 1

    if n < k or n == 0:
        return 0

    k = min(k, n - k)
    if k == n or k == 0:
        return 1

    result = 1
    for n in range(n, n - k, -1):
        result *= n
    for d in range(1, k + 1):
        result //= d

    return result


def chinese_remainder(congruences, primes, M):
    """
    Find x which satisfies (for all i)
    x = congruences[i] (mod primes[i])
    """
    total = 0
    for a, p in zip(congruences, primes):
        m = M // p
        total += a * inverse(m, p) * m

    return total % M


def chooseMod(n, k, M):
    """
    Calculate n choose k mod M
    """
    if n == k == 0:
        return 1

    if n < k or n == 0:
        return 0

    k = min(k, n - k)
    if k == n or k == 0:
        return 1

    primes = factors(M)
    congruences = [0] * len(primes)

    for i, p in enumerate(primes):
        prod = 1

        for ni, ki in zip(digits(n, p), digits(k, p)):
            prod *= choose(ni, ki)

            if prod == 0:
                break
        congruences[i] = prod
    return chinese_remainder(congruences, primes, M)


cases = int(input())
for _ in range(cases):
    n, k, M = [int(x) for x in input().split()]
    print(chooseMod(n, k, M))

## Extended Solution


memo = {}
def C(n, r, p):
    ''' {n choose r} modulo p (p is prime) '''
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    if n >= p: # Lucas theorem
        return C(n/p, r/p, p) * C(n%p, r%p, p) % p
    if (n, r, p) not in memo:
        memo[n, r, p] = (C(n-1, r-1, p) + C(n-1, r, p)) % p
    return memo[n, r, p]

def egcd(a, b):
    ''' finds (x, y) such that a*x + b*y = gcd(a, b) '''
    if b == 0:
        return 1, 0
    else:
        x, y = egcd(b, a % b)
        return y, x - (a / b) * y

def inv(a, n):
    ''' modular inverse of a modulo n '''
    x, y = egcd(a%n, n)
    return x % n

def chinese(a1, m1, a2, m2):
    ''' finds (x, m) such that x == a1 (mod m1), x == a2 (mod m2), 0 <= x < m = m1*m2 '''
    m = m1 * m2
    return (a1 * inv(m2, m1) % m1 * m2 + a2 * inv(m1, m2) % m2 * m1) % m, m

def prime_factorize(n):
    ''' yields all prime-exponent pairs in the prime factorization of n '''
    p = 2
    while p <= n:
        if p * p > n:
            p = n
        e = 0
        while n % p == 0:
            n /= p
            e += 1
        if e:
            yield p, e
        p += 1
####
z = int(input())## test casess
for cas in xrange(z):
        n, r, m = map(int, raw_input().strip().split())

        ans, mod = 0, 1
        for p, e in prime_factorize(m):
            assert e == 1
            assert p < 50
            ans, mod = chinese(ans, mod, C(n, r, p), p)

        print ans
