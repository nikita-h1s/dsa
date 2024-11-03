import time
from collections import defaultdict


def find_combinations_naive(s, m):
    res = 0

    n = len(m)
    for mask in range(1 << n):
        cur_sum = 0
        for i in range(n):
            cur_sum += m[i] if mask & (1 << i) else 0
        res += 1 if cur_sum == s else 0

    return res


def find_combinations(s, m):
    half = len(m) // 2
    a = m[:half]
    b = m[half:]
    x = defaultdict(int)

    n1 = len(a)
    for mask in range(1 << n1):
        cur_sum = 0
        for i in range(n1):
            cur_sum += a[i] if mask & (1 << i) else 0
        x[cur_sum] += 1

    res = 0
    n2 = len(b)
    for mask in range(1 << n2):
        cur_sum = 0
        for i in range(n2):
            cur_sum += b[i] if mask & (1 << i) else 0

        res += x[s - cur_sum]

    return res
