from visualize import visualize


def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
        visualize(arr)


def merge_sort(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge_sort(left[1:], right)

    return [right[0]] + merge_sort(left, right[1:])


def tim_sort(arr):
    min_run = 32
    n = len(arr)

    visualize(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge_sort(
                left=arr[start : midpoint + 1], right=arr[midpoint + 1 : end + 1]
            )
            arr[start : start + len(merged_array)] = merged_array
            visualize(arr)
        size *= 2

    visualize(arr)

    return arr
