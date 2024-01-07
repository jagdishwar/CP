import sys

sys.setrecursionlimit(10 ** 9)


def scc(g, n):
    seen = [False] * n
    q = []

    def dfs(i):
        seen[i] = True
        for j in g[i]:
            if not seen[j]:
                dfs(j)
        q.append(i)

    for i in range(n):
        if not seen[i]:
            dfs(i)

    gT = [[] for _ in range(n)]
    for i in range(n):
        for j in g[i]:
            gT[j].append(i)

    seen = [False] * n

    def rev_dfs(i):
        sc.append(i)
        seen[i] = True
        for j in gT[i]:
            if not seen[j]:
                rev_dfs(j)

    ans = []
    for i in q[::-1]:
        if not seen[i]:
            sc = []
            rev_dfs(i)
            ans.append(sc)
    return ans


N, M = map(int, input().split())
g = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)

SC = scc(g, N)
