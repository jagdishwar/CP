stack=[]
def dfsdeploy(visited,node):
    if node in visited:
        return

    visited[node]=True
    for it in graph[node]:

        if it in visited:
            dfsdeploy(visited,it)
    stack.append(it)
