from visualize import visualize_sorting


def merge_sort(arr, visualize=False):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves.
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], visualize)
    # Recursively sort the left half
    right = merge_sort(arr[mid:], visualize)
    # Recursively sort the right half

    # Merge the two sorted halves.
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
    # Append any remaining elements from the left half
    merged.extend(right[j:])
    # Append any remaining elements from the right half

    if visualize:
        visualize_sorting(merged)

    return merged
