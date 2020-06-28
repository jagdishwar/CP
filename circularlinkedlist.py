class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularlinkedlist:
    def __init__(self):
        self.head=None
    def appendele(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            self.head.next=self.head
        else:
            p=self.head
            while p!=self.head:
                p=p.next
            p.next=newnode
            newnode.next=self.head
    def printele(self):
            p=self.head

            while p:
                print(p.data)
                p=p.next
                if p==self.head:
                    break

clist=circularlinkedlist()
clist.appendele('A')
clist.appendele('B')
clist.appendele('C')
clist.appendele('D')

clist.printele()