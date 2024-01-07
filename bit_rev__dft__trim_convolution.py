mod = 998244353

zeta = pow(3,7*17,mod)
index = 23
zetas = [zeta]
z = zeta
for i in range(23):
    z *= z
    z %= mod
    zetas.append(z)
invzetas = [pow(z,mod-2,mod) for z in zetas]

def bit_rev(f,m):
    fd = [0]*(2**m)
    l = 2**m
    for i in range(len(f)):
        k = 0
        for j in range(m):
            if (1<<j)&i>0:
                k += 1<<(m-j-1)
        fd[k] = f[i]
    return fd

def dft(f, m=None, inv=False):
    if m is None:
        m = 0
        l = 1
        while l<len(f):
            m += 1
            l *= 2
    else:
        l = 2**m
    if m==0:
        return [f[0]]
    fd = bit_rev(f,m)
    s = 1
    t = l//2
    for i in range(1,m+1):
        if not inv:
            z = zetas[index-i]
        else:
            z = invzetas[index-i]
        z1 = 1
        for j in range(s):
            for k in range(t):
                a,b = 2*k*s+j, 2*k*s+j+s
                fd[a], fd[b] = (fd[a] + z1*fd[b])%mod, (fd[a] - z1*fd[b])%mod
            z1 *= z
            z1 %= mod
        t //= 2
        s *= 2
    if inv:
        invl = pow(l,mod-2,mod)
        for i in range(l):
            fd[i] *= invl
            fd[i] %= mod
    return fd


def dft1(f, m=None, inv=False, start=True):
    if m is None:
        m = 0
        l = 1
        while l<len(f):
            m += 1
            l *= 2
    else:
        l = 2**m
    if m==0:
        return [f[0]]
    if start:
        fd = [f[i] if len(f)>i else 0 for i in range(l)]
    else:
        fd = f
    fd0 = dft1(fd[::2],m-1,inv,False)
    fd1 = dft1(fd[1::2],m-1,inv,False)
    if inv:
        zeta1 = pow(zeta, (mod-2)*(2**(index-m)), mod)
    else:
        zeta1 = pow(zeta,2**(index-m),mod)
    zeta2 = 1
    if start and inv:
        invl = pow(l,mod-2,mod)
    for i in range(l):
        j = i
        if j>=l//2:
            j -= l//2
        if start and inv:
            fd[i] = ((fd0[j] + zeta2*fd1[j])*invl)%mod
        else:
            fd[i] = (fd0[j] + zeta2*fd1[j])%mod
        zeta2 *= zeta1
        zeta2 %= mod
    return fd


def trim(A):
    for i in range(len(A)-1,-1,-1):
        if A[i]!=0:
            break
    return A[:i+1]
## convolution Ci=Summationj=0 to i Aj Bi-j
def convolution(A,B,trim=True):
    if trim:
        A = trim(A)
        B = trim(B)
    l1 = len(A)
    l2 = len(B)
    l = l1+l2-1
    m = 0
    ll = 1
    while ll<l:
        ll *= 2
        m += 1
    Ad = dft(A,m)
    Bd = dft(B,m)
    for i in range(ll):
        Ad[i] = (Ad[i]*Bd[i])%mod
    return dft(Ad,inv=True)[:l]

def poly_pow(A,p,trim=True):
    if trim:
        A = trim(A)
    l = (len(A)-1)*p + 1
    Ad = dft(A)
    m = 0
    ll = 1
    while ll<l:
        ll *= 2
        m += 1
    Ad = dft(A,m)
    Bd = [pow(a,p,mod) for a in Ad]
    return dft(Bd,inv=True)[:l]
