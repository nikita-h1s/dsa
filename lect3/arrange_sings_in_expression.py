def arrange_sings_in_expression(sequence):
    n = len(sequence)

    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = sequence[i]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            for k in range(i, j):
                matrix[i][j] = max(matrix[i][j],
                                   matrix[i][k] + matrix[k + 1][j],
                                   matrix[i][k] * matrix[k + 1][j]
                                   )

    return matrix[0][n-1]


print(arrange_sings_in_expression([1, 4, 2, 3, 0, 5, 1, 2]))