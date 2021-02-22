import collections
class graph:
    def __init__(self,adjacency=None):
            if adjacency is None:
                adjacency={}
            self.adjacency=adjacency

def bfs(graph,startnode):
    seen,queue=set([]),collections.deque([startnode])
    while queue:
        vertex=queue.pop(0)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


adjacency={
    "a":set(["b","c"]),
    "b":set(["a","d"]),
    "c":set(["a","d"]),
    "d":set(["e"]),
    "e":set(["a"])


}
bfs(graph,"a")