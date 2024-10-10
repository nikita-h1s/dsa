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

visited = set()
def dfs(v, ts):
    visited.add(v)
    for u, w in graph[v]:
        if u not in visited:
            dfs(u, ts)

    ts.append(v)


def top_sort():
    ts = []
    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i, ts)

    ts.reverse()
    return ts


def min_path(v):
    d = [float('inf')] * n
    ts = top_sort()
    d[ts[0]] = 0

    for v1 in ts:
        for v2, w in graph[v1]:
            d[v2] = min(d[v2], d[v1] + w)

    return d[v]
