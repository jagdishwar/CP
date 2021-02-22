from collections import defaultdict
matrix=[[2,1],[3,4],[3,2]]
graph=defaultdict(list)
for u,v in matrix:
        graph[u].append(v)
        graph[v].append(u)

print(graph)
print(graph.items())
start=matrix[0][0]
for key,value in graph.items():
    if len(value)==1:
        start=key
        break

#dfs to connect the graph
nodes=[]
seen=set()
def dfs(node):
    seen.add(node)
    for it in graph[node]:
        if it not in seen:
            dfs(it)
    nodes.append(node)
dfs(start)
print(nodes)




