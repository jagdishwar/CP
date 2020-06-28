class DLL:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}
        self.head = DLL(0, 0)
        self.tail = DLL(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removethenode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def aappendtohead(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

    def removefromtail(self):
        if len(self.hash) == 0:
            return
        tail_node = self.tail.prev
        del self.hash[tail_node.key]
        self.removethenode(tail_node)

    # @return an integer
    def get(self, key):
        if key in self.hash:
            node = self.hash[key]
            va = node.value
            self.removethenode(node)
            self.aappendtohead(node)
            return va
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hash:
            node = self.hash[key]
            self.removethenode(node)
            self.aappendtohead(node)
            node.value = value
        else:
            if len(self.hash) >= self.capacity:
                self.removefromtail()
            node = DLL(key, value)
            self.hash[key] = node
            self.aappendtohead(node)


