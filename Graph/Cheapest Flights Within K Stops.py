from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        d = defaultdict(list)
        for u, v, w in flights:
            d[u].append((w, v))
        list1 = [(0, -1, src)]
        dist = {}

        while list1:
            cost, k, node = heappop(list1)
            if k > K:
                continue
            if node == dst:
                return cost

            for edgeCost, next_node in d[node]:
                if dist.get((k + 1, next_node), float('inf')) > edgeCost + cost:
                    dist[(k + 1, next_node)] = edgeCost + cost
                    heappush(list1, (edgeCost + cost, k + 1, next_node))
        return -1 