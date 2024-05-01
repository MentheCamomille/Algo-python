from visualize import visualize_sorting


def merge_sort(arr, visualize=False):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], visualize)
    right = merge_sort(arr[mid:], visualize)

    merged = []

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    if visualize:
        visualize_sorting(merged)

    return merged
