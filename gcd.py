def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a=12
b=45
if b>a:
    a,b=b,a

print(gcd(a,b))
### iterative

a=12
b=45
if b>a:
    a,b=b,a

while b>0:
    a,b=b,a%b
print(a)
