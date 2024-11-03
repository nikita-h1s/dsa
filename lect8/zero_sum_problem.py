def find_nums_naive(m, target_sum=0):
    res_arr = []

    for i in range(len(m)):
        for j in range(len(m)):
            for k in range(len(m)):
                for l in range(len(m)):
                    combo = [m[i], m[j], m[k], m[l]]

                    if sum(combo) == target_sum:
                        res_arr.append(combo)

    return len(res_arr)


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    res = []

    while left <= right:
        mid = (left + right) // 2

        if target < arr[mid][0]:
            right = mid - 1
        elif target > arr[mid][0]:
            left = mid + 1
        else:
            res.append(mid)
            i = mid - 1
            while i >= 0 and arr[i][0] == target:
                res.append(i)
                i -= 1
            i = mid + 1
            while i < len(arr) and arr[i][0] == target:
                res.append(i)
                i += 1
            break

    return res if res else None


def find_nums(m, target_sum=0):
    arr = []

    for i in range(len(m)):
        for j in range(len(m)):
            combo = [m[i], m[j]]

            arr.append([sum(combo), combo])

    arr.sort(key=lambda x: x[0])

    results = []

    for left in arr:
        complement = target_sum - left[0]
        indices = binary_search(arr, complement)

        if indices:
            for idx in indices:
                results.append(left[1] + arr[idx][1])

    return len(results)
