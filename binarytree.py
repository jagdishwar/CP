class bstnode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert_node(self,root,node):
        if root=None:
            root=node
        else:
            if root.value<node.value:
                if root.right==None:
                    root.right=node
                else:
                    insert_node(root.right,node)
            else:
                if root.left==None:
                    root.left=node
                else:
                    insert_node(root.left,node)
