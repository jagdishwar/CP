##aX+bY=c (find x and y)
#aX0+BY0=g (extended gcd) mul *c/g
#X=X0*c//g and y==Y0*c//g
# if c%g==0 soln exist
#linear diophantine equation
def extendedgcd(a,b):
    if b==0:
        return a,1,0
    gcd,x0,y0=extendedgcd(b,a%b)
    x=y0
    y=(x0-(a//b)*y0)
    return gcd,x,y

def LDE(a,b,c):
    gcd,x0,y0=extendedgcd(a,b)
    if c%gcd!=0:
        return False
    x=x0*c//gcd
    y=y0*c//gcd
    if a<0:
        x=-x
    if b<0:
        y=-y

    return x,y
#ax+by=c
a,b,c=map(int,input().split())
print(LDE(a,b,c))




