def fib_memo(n, memo={}):
    if n == 0 or n == 1:
        return 1

    if n in memo: return memo[n]

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


def fib_tab(n):
    data = [0, 1]
    data += [0] * (n - 1)

    for i in range(2, n + 1):
        data[i] = data[i - 1] + data[i - 2]

    return data[n]


def fib_tab_optimized(n):
    if n in (0, 1):
        return n

    prev2, prev1 = 0, 1

    for i in range(n - 1):
        temp = prev1
        prev1 = prev2 + prev1
        prev2 = temp

    return prev1

