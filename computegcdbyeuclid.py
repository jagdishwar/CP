def computegcd(a,b):
    if b==0:
        return a
    return computegcd(b,a%b)


p=computegcd(100,20)
print(p)