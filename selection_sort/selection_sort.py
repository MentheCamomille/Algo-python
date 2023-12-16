from visualize import visualize_sorting


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        # Assume the current element is the minimum
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # If a smaller element is found
                min_index = j
                # Update the index of the minimum

        # Swap the current element with the minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        visualize_sorting(arr)

    return arr
