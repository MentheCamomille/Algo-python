from visualize import visualize


def leonardo(k):
    if k < 2:
        return 1
    return leonardo(k - 1) + leonardo(k - 2) + 1


def heapify(arr, start, end):
    i = start
    j = 0
    k = 0

    while k < end - start + 1:
        if k & 0xAAAAAAAA:
            j = j + i
            i = i >> 1
        else:
            i = i + j
            j = j >> 1

        k = k + 1

    while i > 0:
        j = j >> 1
        k = i + j
        while k < end:
            if arr[k] > arr[k - i]:
                break
            arr[k], arr[k - i] = arr[k - i], arr[k]
            k = k + i

        i = j


def smooth_sort(arr):
    n = len(arr)

    p = n - 1
    q = p
    r = 0

    while p > 0:
        visualize(arr)
        heapify(r, q)
        visualize(arr)

        if leonardo(r) == p:
            r = r + 1
        else:
            r = r - 1
            q = q - leonardo(r)
            heapify(r, q)
            q = r - 1
            r = r + 1

        arr[0], arr[p] = arr[p], arr[0]
        p = p - 1

    visualize(arr)

    for i in range(n - 1):
        j = i + 1
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1

    visualize(arr)

    return arr
