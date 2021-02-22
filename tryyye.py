class queue:
    def __init__(self):

        self.list1=[]

    def dequeue(self):
        return self.list1.pop(0)

    def addd(self,val):
        self.list1.append(val)
        return self.list1



op=queue()
op.addd(1)
op.addd(2)
op.addd(3)
op.addd(4)
print(op.dequeue())
print(op.dequeue())
print(op.addd(5))

