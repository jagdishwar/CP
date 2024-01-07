import sys
input = sys.stdin.readline
import sys
def input():
    return sys.stdin.readline().rstrip()
# 単位元とseg_funcを設定する
from fractions import gcd
class seg():
    def __init__(self,init_val):
        self.n=len(init_val)
        self.ide_ele=0 #単位元
        self.num=2**(self.n-1).bit_length() #n以上の最小の2のべき乗
        self.seg=[self.ide_ele]*2*self.num
        for i in range(self.n):
            self.seg[i+self.num-1]=init_val[i]
        for i in range(self.num-2,-1,-1):
            self.seg[i]=self.seg_func(self.seg[2*i+1],self.seg[2*i+2])
    def seg_func(self,a,b):
        #return a+b #0
        #return a*b #1
        #return gcd(a,b) #0
        return max(a,b) #-1か-10**10 (十分小さいもの)
        #return min(a,b) #10**10 (十分大きいもの)
    def update(self,k,x):
        k+=self.num-1
        self.seg[k]=x
        while k:
            k=(k-1)//2
            self.seg[k]=self.seg_func(self.seg[k*2+1],self.seg[k*2+2])
    def query(self,p,q): #O(logN)
        if q<=p:return self.ide_ele
        p+=self.num-1
        q+=self.num-2
        self.res=self.ide_ele
        while q-p>1:
            if p&1==0:
                self.res=self.seg_func(self.res,self.seg[p])
            if q&1==1:
                self.res=self.seg_func(self.res,self.seg[q])
                q-=1
            p=p//2
            q=(q-1)//2
        if p==q:self.res=self.seg_func(self.res,self.seg[p])
        else:self.res=self.seg_func(self.seg_func(self.res,self.seg[p]),self.seg[q])
        return self.res



dp=[0]*(n+1)
segdp=seg(dp)


## segment tree useful

class SegmentTree:

    def __init__(self, n, fn=lambda x, y: min(x, y), unity=(1 << 31) - 1):
        self.n = 1
        while self.n < n:
            self.n *= 2

        self.arr = [unity] * (2 * self.n - 1)
        self.fn = fn
        self.unity = unity

    def update(self, i, x):
        k = self.n + i - 1
        self.arr[k] = x

        while k > 0:
            k = (k - 1) // 2
            self.arr[k] = self.fn(self.arr[2 * k + 1], self.arr[2 * k + 2])

    def query(self, l, r):
        return self._inner_query(l, r, 0, 0, self.n)

    def _inner_query(self, l, r, k, il, ir):
        if ir <= l or r <= il:
            return self.unity

        elif l <= il and ir <= r:
            return self.arr[k]

        vl = self._inner_query(l, r, k * 2 + 1, il, (il + ir) // 2)
        vr = self._inner_query(l, r, k * 2 + 2, (il + ir) // 2, ir)
        return self.fn(vl, vr)

    def __str__(self):
        return self.arr[0: 2 * self.n].__str__()


    
