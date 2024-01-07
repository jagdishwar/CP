n=int(input())
parent={node:node for node in range(n+1)}
rank=[0]*(n+1)
size=[1]*(n+1)

def find(node):
    if parent[node]==node:
        return node
    return find(parent[node])

def union(a,b):
    root_a=find(a)
    root_b=find(b)
    if root_a==root_b:
        return
    ##path comprehension
    elif rank[root_a]>rank[root_b]:
        parent[root_b]=root_a
        size[root_a]+=size[root_b]
    else:
        if rank[root_a]==rank[root_b]:
            rank[root_b]+=1
        parent[root_a]=root_b
        size[root_b]+=size[root_a]
def same(a,b):
    if find(a)==find(b):
        return True
    return False

def members(node):
    root=find(node)
    return {i for i in range(n) if parent[i]==root}

def sizes(node):
    return size[find(node)]
