#aX+bY=gcd(a,b)
#bX1+(a%b)Y1=gcd {a%b=a-[a//b]*b}
#bX1+{a-[a//b]*b}Y1=gcd
#aY1+b(X1-Y1*[a//b])=gcd
# i.e x=Y1 and y=(X1-Y1*[a//b])
"""
def extendeuclid(a,b,x,y):
    if b==0:
        x=1
        y=0
        return a
    x1=0
    y1=0
    gcd=extendeuclid(b,a%b,x1,y1)
    x=y1
    y=(x1-y1*(a//b))
    return gcd"""

def extendedGCD(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extendedGCD(b, a%b)

    x, y = (y1,x1 - (a // b) * y1)

    return gcd, x, y

def inv(a,n):
    gcd,x,y=extendedGCD(a%n,n)
    return x%n

print(inv(63,57))
