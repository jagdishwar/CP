##Cycle in Directed Graph

def dfscycle(node,visited,rec):
            visited[node]=True
            rec[node]=True
            for next_node in graph[node]:
                if not visited[next_node] and dfscycle(next_node,visited,rec):
                    return True
                elif rec[next_node]:
                    return True
            rec[node]=False
    
            return False
            
visited=[False]*(numCourses+1)
rec=[False]*(numCourses+1)
for i in range(numCourses):
    if not visited[i]: 
        if dfscycle(i,visited,rec):
            return False


##Cycle in Undirected Graph


graph = [[] for i in range(A+1)]
for u,v in B:
            graph[u].append(v)
            graph[v].append(u)

# Defining DFS.
def dfs(v, parent = -1):
    visited.add(v)
    for node in graph[v]:
        if node not in visited:
            if dfs(node, v):
                return True
        elif node != parent:
            return True
    return 0

        # Main function call.
visited = set()
for v in range(A+1):
    if v not in visited:
        if dfs(v):
            return 1
return 0
