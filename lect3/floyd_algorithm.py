inf = float('inf')
adj_matrix = [[0, inf, 3, inf], [2, 0, inf, 1], [inf, 7, 0, 1], [6, inf, inf, 0]]


def floyd_algorithm(matrix):
    n = len(matrix)
    closure = matrix.copy()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = min(closure[i][j], closure[i][k] + closure[k][j])

    return closure
