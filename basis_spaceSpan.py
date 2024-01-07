class XorBasisSpace:
    '''
    xorの線形空間のクラス
    add(x)でxを追加（従属な場合は追加されない）
    isIndipendent(x)でxが独立か従属かを判定
    '''
    def __init__(self):
        self.base = []
    
    def add(self,x):
        for y in sorted(self.base,reverse=True):
            x = min(x,x^y)
        if x:
            self.base.append(x)
            return True
        else:
            return False
    
    def isIndependent(self,x):
        '''
        xが独立->True
        xが従属->False
        '''
        for y in sorted(self.base,reverse=True):
            x = min(x,x^y)
        if x:
            return True
        else:
            return False

xbs = XorBasisSpace()
xbs.add(bit)
    
