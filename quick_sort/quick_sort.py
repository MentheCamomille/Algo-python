from visualize import visualize_sorting


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]

    visualize_sorting(arr)

    return quick_sort(less) + [pivot] + quick_sort(greater)
