class TrieNode:
    def __init__(self,letter):
        self.letter=letter
        self.child={}
        self.end=False


class Trie:
    def __init__(self):
        self.root=TrieNode('*')
    def insert_node(self,word):
        p=self.root.child
        for i in word:
            if i not in p:
                node=TrieNode(i)
                p[i]=node
            else:
                node=p[i]
            p=node.child
            nie=node
        nie.end=True
    def search(self,word):
        p=self.root.child
        for i in word:
            if i not in p:
                return False
            else:
                node=p[i]
            p=node.child
        return p.end


    def startwithprefix(self,prefix):
        p=self.root.child
        for i in prefix:
            if i not in p:
                return False
            else:
                node=p[i]
                p=node.child
        return True



