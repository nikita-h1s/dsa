### Failed bfs approach
# from collections import deque
#
# graph = [
#     [(4, 2)],  # 0
#     [(0, 1), (2, 1), (4, 4), (5, 3)],  # 1
#     [(5, 1)],  # 2
#     [],  # 3
#     [(3, 3), (7, 1)],  # 4
#     [(3, 5), (6, 2)],  # 5
#     [(3, 2)],  # 6
#     [(3, 1)],  # 7
# ]
#
#
# def shortest_robust_path_bfs(graph, k, s, t):
#     n = len(graph)
#     matrix = [[float('inf') for _ in range(k)] for _ in range(n)]
#     matrix[s][0] = 0
#
#     queue = deque([[node for node in graph[s]]])
#     cur_lvl = 0
#     cur_idx = s
#     while queue and cur_lvl < k:
#         new_lvl = deque([])
#         for i in range(len(queue)):
#             pack = queue.popleft()
#             if pack:
#                 node, node_w = pack
#                 cur_w = matrix[cur_idx][cur_lvl] + node_w
#                 if matrix[node][cur_lvl] > cur_w:
#                     matrix[node][cur_lvl] = cur_w
#
#             new_lvl.append((graph[node]))
#
#         cur_lvl += 1
#         queue = new_lvl
#
#     return matrix


graph = [
    [(4, 2)],  # 0
    [(0, 1), (2, 1), (4, 4), (5, 3)],  # 1
    [(5, 1)],  # 2
    [],  # 3
    [(3, 3), (7, 1)],  # 4
    [(3, 5), (6, 2)],  # 5
    [(3, 2)],  # 6
    [(3, 1)],  # 7
]


def shortest_robust_path(graph, start, target, k):
    n = len(graph)
    matrix = [[float('inf')] * (k + 1) for _ in range(n)]
    matrix[start][0] = 0

    for m in range(k):
        for v1 in range(n):
            for v2, w in graph[v1]:
                matrix[v2][m + 1] = min(matrix[v2][m + 1], matrix[v1][m] + w)

    return min(matrix[target])


print(shortest_robust_path(graph, 0, 3, 3))
