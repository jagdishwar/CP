from collections import defaultdict
import heapq
def solve( A, B):
    # prim
    connected = {1}
    adj = defaultdict(list)

    for u, v, w in B:
        adj[u].append((w, v))
        adj[v].append((w, u))
    pending = adj[1][:]
    heapq.heapify(pending)
    cost = 0
    while len(pending) > 0:
        print([pending])
        w, u = heapq.heappop(pending)
        if u in connected:
            continue
        connected.add(u)
        cost += w

        for ww, v in adj[u]:

            if v not in connected:
                heapq.heappush(pending, (ww, v))

    print(connected)
    return cost
A = 4
B =[[1, 2, 1],[2, 3, 4],[1, 4, 3],[4, 3, 2],[1, 3, 10]]

print(solve(A,B))
