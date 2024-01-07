##k to n points
def dikstra(k):
    dist={i:float('inf') for i in range(1,n+1)}
    dist[k]=0
    queue=[(k,0)]
    heapq.heapify(queue)
    while queue:
        cur_node,cur_weight=heapq.heappop(queue)
        for nxt_node,nxt_weight in graph[cur_node]:
            if nxt_weight+cur_weight < dist[nxt_node]:
                dist[nxt_node]=nxt_weight+cur_weight
                heapq.heappush(queue,(nxt_node,dist[nxt_node]))
    return dist

#n to n points

dist=[[float('inf')]*(n+1) for _ in range(n+1)]


for i in range(n-1):
    u,v=map(int,input().split())
    dist[u-1][v-1]=dist[v-1][u-1]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

