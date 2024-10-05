def matrix(n):
    matrix = []

    for i in range(n + 1):
        row = []
        for j in range(i + 1):
            row.append(1)
        matrix.append(row)

    return matrix

def bin_coef(n, k):
    if k > n:
        return None

    mat = matrix(n)

    for i in range(1, n + 1):
        for j in range(1, i):
            mat[i][j] = mat[i - 1][j - 1] + mat[i - 1][j]

    return mat[n][k]

print(bin_coef(5, 2))