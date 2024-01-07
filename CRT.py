# O(N * Log(lcm(m1, m2, ..., mn))) - General Chinese Remainder Theorem.
#
# Considering the following family of linear congruences:
#
# t = a1 (mod m1)
# t = a2 (mod m2)
# ...
# t = an (mod mn)
#
# Returns the smallest non-negative solution modulo lcm(m1, m2, ..., mn). Returns -1 if there is no solution.
#
# The family of linear congruences has a solution if and only if every pair of linear congruences is consistent.
# A pair of linear congruences is consistent if a1 = a2 (mod gcd(m1, m2)).
#
# t = a1 (mod m1) ---> t - a1 = m1 * x
# t = a2 (mod m2) ---> t - a2 = m2 * y
#
# a1 + m1 * x = a2 + m2 * y
# m1 * x - m2 * y = a2 - a1
# m1 * x + m2 * (-y) = a2 - a1
#
# x = x1 + k * m2 / gcd(m1, m2)
# y = -y1 + k * m1 / gcd(m1, m2)
#
# t - a1 = m1 * (x1 + k * m2 / gcd(m1, m2))
# t - a1 = m1 * x1 + lcm(m1, m2) * k
# t - (a1 + m1 * x1) = lcm(m1, m2) * k ---> t = a1 + m1 * x1 (mod lcm(m1, m2))
#
# t - a2 = m2 * (-y1 + k * m1 / gcd(m1, m2))
# t - a2 = -m2 * y1 + lcm(m1, m2) * k
# t - (a2 - m2 * y1) = lcm(m1, m2) * k ---> t = a2 - m2 * y1 (mod lcm(m1, m2))
def extendedgcd(a,b):
    if b==0:
        return a,1,0
    gcd,x0,y0=extendedgcd(b,a%b)
    x=y0
    y=x0-(a//b)*y0
    return gcd,x,y

def LDE(a,b,c):
    gcd,x0,y0=extendedgcd(a,b)
    if c%gcd!=0:
        return 0,0,0
    x=x0*(c//gcd)
    y=y0*(c//gcd)
    if a<0:
        x=-x
    if b<0:
        y=-y
    return gcd,x,y

def CRT(A,M):
    # Making 0 <= ai < mi.
    for i in range(len(A)):
        A[i]=( (A[i] % M[i]) + M[i]) % M[i]
    a1,m1=0,1
    for i in range(len(A)):
        a2,m2=A[i],M[i]
        # Solving n1 * x + n2 * (-y) = a2 - a1
        gcd,x1,y1=LDE(m1,m2,a2-a1)
        if gcd==0:
            return (-1,0)# No solution.
        # Calculating lcm(m1, m2).
        lcm=(m1*m2)//gcd
        # Updating answer.
        a1 = ((a1 + m1 * x1) % lcm + lcm) % lcm
        m1=lcm


    return (a1,m1)
A=[1,2,5]
M=[2,3,7]
print(CRT(A,M))


