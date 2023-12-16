from visualize import visualize_sorting


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
            visualize_sorting(arr)
        arr[j + 1] = current
        visualize_sorting(arr)

    return arr
