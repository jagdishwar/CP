dict1={}

dict1['a']=0
dist=[False]*len()+1
while len(dict1)>0:
    s=dict1.pop(0)
    dist1,node=a
    for it in graph[node]:
        if dist1[it]>dist1[node]+weight:
            if dist1[node]!=float('inf'):
                dict1.pop(node)
            dist[it]=dist[node]+weight
            dict1[it] = dist[node] + weight





