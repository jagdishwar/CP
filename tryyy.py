import collections
import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        graph = collections.defaultdict(list)
        for val in B:
            graph[val[0]].append(val[1])

        def dfsdeploy(node, visited):
            visited[node] = True

            for it in graph[node]:
                if not visited[it]:
                    dfsdeploy(it, visited)
            return

        visited = [False] * (len(A) + 1)
        source = []

        for i in range(1, len(A) + 1):
            if not visited[i]:
                source.append(i)
                dfsdeploy(i, visited)

        visited = [False] * (len(A) + 1)

        cities = [[] for i in source]

        def dfsdeploy(node, visited, i):
            visited[node] = True
            cities[i].append(node)
            for it in graph[node]:
                if not visited[it]:
                    dfsdeploy(it, visited, i)
            return

        for i in range(len(source)):
            if not visited[source[i]]:
                dfsdeploy(source[i], visited, i)

        starting = []
        for city in cities:
            minvalue = float('inf')
            point = 0
            for key in city:
                if minvalue > A[key - 1]:
                    minvalue = A[key - 1]
                    point = key
            starting.append(point)

        graph = collections.defaultdict(list)
        for u, v, w in B:
            graph[u].append((v, w))
            graph[v].append((u, w))
        pack = []
        for K in starting:
            list1 = [(A[K - 1], K)]
        dist = {i: float('inf') for i in range(1, len(A) + 1)}
        dist[K] = A[K - 1]
        while len(list1):
            curr_weight, node = heapq.heappop(list1)

            for next_node, in_cost in graph[node]:

                if in_cost + curr_weight + in_cost < dist[next_node]:
                    heapq.heappush(list1, ((in_cost + curr_weight + in_cost), next_node))
                    dist[next_node] = in_cost + curr_weight + in_cost

        for key, value in dist.items():
            if value != float('inf'):
                pack.append(value)

    return pack





