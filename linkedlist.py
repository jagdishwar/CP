class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def print(self):
        p=self.head
        while p:
            print(p.data)
            p=p.next
    def appendele(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        p=self.head
        while p.next:
            p=p.next
        p.next=new_node
    def prepend(self,data):
        nwe_node=node(data)
        if self.head is None:
            return
        nwe_node.next=self.head
        self.head=nwe_node
    def insertion(self,previous,data):
        new_node=node(data)
        if previous is None:
            return
        new_node.next=previous.next
        previous.next=new_node
    def deletelement(self,data):
        p=self.head
        if p and p.data==data:
            self.head=p.next
            p=None
            return
        prev=None
        while p and p.data!=data:
            prev=p
            p=p.next
        prev.next=p.next
        p.next=None
    def deletebypos(self,pos):
        p=self.head
        if pos==0:
            self.head=p.next
            self.head=None
        prev=None
        count=0
        while pos!=count and p:
            prev=p
            count+=1
            p=p.next
        prev.next=p.next
        p=None
    def swappping(self,key1,key2):
        p1=self.head
        prev1=None

        while p1.data!=key1 and p1:
            prev1=p1
            p1=p1.next
        prev2=None
        p2=self.head

        while p2.data!=key2 and p2:
            prev2=p2
            p2=p2.next
        if prev1:
            prev1.next=p2
        else:
            self.head=p2
        if prev2:
            prev2.next=p1
        else:
            self.head=p1
        print(prev1.data,'this is data prev1')
        print(prev2.data,'htis is data prev2')
        p1.next,p2.next=p2.next,p1.next
    def helper_zone(self,node):
        if node is None:
            return None
        else:
            print('data'+node.data)
    def reverselinkedlist(self):
        p=self.head
        prev=None
        while p:
            nxt=p.next#we need beacuse the we store the next node beacuse it missup the previous node
            p.next=prev#
            prev=p
            p=nxt
        self.head=prev

    def mergetwolinkedlist(self,listt):
        p=self.head
        q=listt.head
        s=None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data<=q.data:
                s=p
                p=s.next
            else:
                s=q
                q=s.next
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            s.next=q
        if not q:
            s.next=p
    def removedublicates(self):
        p=self.head
        prev=None
        dict1={}
        while p:
            if p.data in dict1:
                prev.next=p.next
                p=None
                #remove the element
            else:
                dict1[p.data]=1
                prev=p
            p=prev.next#i dont know why this is happening #ok i got it now is that change that happens at the stage
    def  print_nth_lastnode(self,n):
        p=self.head
        totallength=0
        while p:
            totallength+=1
            p=p.next
        print(totallength)
        q=self.head
        while q:
            if totallength==n:
                print(q.data)
                break
            totallength-=1
            q=q.next
        print(q.data)
    def countnumberofoccurances(self,key):
        p=self.head
        count=0
        while p :
            if p.data is key:
                count+=1
            p=p.next
        print(count)
    def rotatingbyposition(self,pos):
        p=self.head
        q=self.head
        count=1
        while q.next:
            q=q.next
        while count!=pos and p:
            count+=1
            p=p.next
        q.next=self.head
        self.head=p.next
        p.next=None
    def paladramma(self):
        p=self.head
        str1=""
        while p:
            str1+=p.data
            p=p.next
        return str1==str1[::-1]

    def move_tail(self):
        dummy=node(0)
        current=dummy
        print(current)
        print(dummy)
        """p=self.head
        prev=None
        while p.next:
                prev=p
                p=p.next
        p.next=self.head
        prev.next=None
        self.head=p








"""



llist_1 = linkedlist()
llist_2 = linkedlist()
llist_1.appendele('A')
llist_1.appendele('B')
llist_1.appendele('C')
llist_1.appendele('D')
"""llist_1.appendele(1)
llist_1.appendele(2)
llist_1.appendele(1)
llist_1.appendele(1)
llist_1.appendele(10)
llist_1.appendele(3)
llist_1.appendele(12)

llist_2.appendele(2)
llist_2.appendele(3)
llist_2.appendele(4)
llist_2.appendele(6)
llist_2.appendele(11)
"""
print('%^^%%&^^^^^^^^^^^^')

"""print('$$$$$$$$$$$$$$')
llist.prepend('E')
llist.print()
llist.insertion(llist.head.next,'Y')
print('BYCNNAGED')
llist.print()
print('deletionofeleemnt')
llist.deletelement('E')
llist.print()
print('deletionbypostion')
llist.deletebypos(2)
llist.print()
print('by replacing')
llist.swappping('Y','C')
llist.print()
print('*******************')
llist.reverselinkedlist()
llist.print()
print('&&&&&&&&&&&&&&&&&&')
#llist_1.mergetwolinkedlist(llist_2)
llist_1.removedublicates()
llist_1.print()
#print"""
'''print('%%%%%%%%%%%%%%%%%%%%%%%%%')
print(llist_1.print_nth_lastnode(3))
print('####################')
llist_1.countnumberofoccurances(1)
print('fuckc this world')
llist_1.rotatingbyposition(4)
llist_1.print()'''
"""print(llist_1.paladramma())
print('$$$$$$$$$$$$$$')"""
llist_1.move_tail()