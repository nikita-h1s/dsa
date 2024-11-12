adj_matrix = [[0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [1, 0, 1, 0]]


def transitive_dfs(matrix):
    row_mat = len(matrix)
    col_mat = len(matrix[0])
    closure = [matrix[i] for i in range(row_mat)]
    adj_list = {i: [] for i in range(row_mat)}

    for i in range(row_mat):
        for j in range(col_mat):
            if matrix[i][j]:
                adj_list[i].append(j)

    def dfs(start, node, vis):
        for neighbor in adj_list[node]:
            if neighbor not in vis:
                vis[neighbor] = True
                closure[start][neighbor] = 1
                dfs(start, neighbor, vis)

    for i in range(row_mat):
        visited = {}
        dfs(i, i, visited)

    return closure


def warshall(matrix):
    closure = matrix.copy()
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure


print(warshall(adj_matrix))
