def gcd(A, B):
        if  B == 0:
            return A
        Arun = A % B
        return gcd(B, Arun)

print(gcd(10, 12))