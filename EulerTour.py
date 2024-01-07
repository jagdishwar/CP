graph=[[1,2],[],[3],[]]
intime=[-1]*(len(graph))
outtime=[-1]*(len(graph))
ET=[-1]*((2*len(graph))+1)
curtime=0
def dfs(node):
    global curtime
    curtime+=1
    ET[curtime]=node
    intime[node]=curtime
    for nxt_node in graph[node]:
            dfs(nxt_node)
    curtime+=1
    ET[curtime] =node
    outtime[node]=curtime

dfs(0)
print(intime)
print(outtime)
print(ET)
