strx='great'
stry='eatgr'
def solve(l1,r1,l2,r2):
    if r1-l1==1:
        return strx[l1]==stry[l2]
    if sorted(strx[l1:r1])!=sorted(stry[l2:r2]):
        return False
    for k in range(1,r1-l1):
        if solve(l1,l1+k,l2,l2+k) and solve(l1+k,r1,l2+k,r2) or \
           solve(l1,l1+k,r2-k,r2) and solve(l1+k,r1,l2,r2-k):
            return True
solve(0,len(strx),0,len(stry))




