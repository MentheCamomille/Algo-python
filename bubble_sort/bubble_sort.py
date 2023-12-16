from visualize import visualize_sorting


def bubble_sort(arr):
    permutation = True
    for j in range(len(arr) - 1):
        if permutation:
            permutation = False
        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                permutation = True
            visualize_sorting(arr)
    return arr
