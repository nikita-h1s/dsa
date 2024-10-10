from collections import defaultdict

n = 8
graph = [
    [(4, 2)],
    [(0, 1), (2, 1), (4, 4), (5, 3)],
    [(5, 1)],
    [],
    [(3, 3), (7, 1)],
    [(3, 5), (6, 2)],
    [(3, 2)],
    [(3, 1)],
]
visited = [False] * n


def count_paths(s, t):
    memo = defaultdict(int)
    memo[s] = 1
    t_sort = top_sort()

    def util():
        for v1 in t_sort:
            for v2, _ in graph[v1]:
                memo[v2] += memo[v1]

        return memo[t]

    return util()


def top_sort():
    ts = []
    visited = set()

    def dfs(v):
        visited.add(v)
        for u, _ in graph[v]:
            if u not in visited:
                dfs(u)

        ts.append(v)

    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)

    ts.reverse()
    return ts


print(count_paths(1, 3))
