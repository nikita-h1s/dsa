passages = [(1, 2), (2, 3), (1, 3), (3, 1)]
n = 3


def matrix(n, passages):
    matrix = [[0] * (n + 1) for _ in range(n+1)]
    for i in range(len(passages)):
        n1, n2 = passages[i]
        matrix[n1][n2] = 1
    return matrix


def multiply_matrix(m1, m2):
    res_matrix = []
    rows = len(m1)
    cols = len(m1[0])
    cur_sum = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            for i in range(cols):
                cur_sum += m1[r][i] * m2[i][c]
            row.append(cur_sum)
            cur_sum = 0
        res_matrix.append(row)

    return res_matrix


def binary_power(matrix, k):
    if k == 1:
        return matrix

    half_power = binary_power(matrix, k // 2)
    if k % 2 == 0:
        return multiply_matrix(half_power, half_power)
    else:
        return multiply_matrix(multiply_matrix(half_power, half_power), matrix)


def count_paths(k):
    mat = matrix(n, passages)
    res = binary_power(mat, k)

    return res


print(count_paths(3))