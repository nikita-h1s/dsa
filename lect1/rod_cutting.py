prices = [None, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

results = [None] * (len(prices) + 1)
def rod_cutting_down(n):
    if results[n] is not None:
        return results[n]

    res = 0
    for i in range(1, n+1):
        res = max(prices[i] + rod_cutting_down(n-i), res)

    results[n] = res
    return res

print(rod_cutting_down(3))



results2 = [None] * (len(prices) + 1)
splits = [0] * (len(prices) + 1)
def rod_cutting_up(n):
    results2[0] = 0

    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            split = prices[j] + results2[i - j]
            if split > res:
                res = split
                splits[i] = j

        results2[i] = res

    return results2[n]


print(rod_cutting_up(6))
