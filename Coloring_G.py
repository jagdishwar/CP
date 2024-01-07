# bipartite Graph
colors=[-1]*(n)
queue=deque([0])
colors[0]=0
while queue:
    node=queue.pop()
    for nxt_node in graph[node]:
        if colors[nxt_node]==-1:
            colors[nxt_node]=1-colors[node]
            queue.append(nxt_node)

