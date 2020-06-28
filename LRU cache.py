class DLL:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
class LRUcache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.head=DLL(-1,-1)
        self.tail=self.head
        self.hashtable={}
        self.length=0

    def get(self,key):
        if key in self.hashtable:
            node=self.hash[key]
            value=node.val
            while node.next:
                node.prev.next=node.next
                node.next.prev=node.prev
                self.tail.next=node
                node.prev=self.tail
                node.next = None
                self.tail=node
            return value
        else:
            return -1

    def put(self,key:int,value:int):
        if key not in hash:
            node=DLL(key,value)
            self.hash[key]=node
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
            self.length+=1
            if self.length>self.capacity:
                remove=self.head.next
                self.head.next=self.head.next.next
                self.head.next.prev=self.head
                del self.hash[remove.key]
                self.length-=1

        else:
            node=self.hash[key]
            while node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node






