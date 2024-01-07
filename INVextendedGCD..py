
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


print(inv(13,57))
