from visualize import visualize_sorting


def heapify(arr, n, i):
    largest = i
    # Initialize the largest as the current root
    left = 2 * i + 1
    # Calculate the index of the left child
    right = 2 * i + 2
    # Calculate the index of the right child

    # If the left child exists and greater than current largest
    if left < n and arr[i] < arr[left]:
        largest = left

    # If right child exists and greater than current largest
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not the current node, swap them
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        visualize_sorting(arr)
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # Get the length of the array

    # Build a max heap by heapifying all non-leaf nodes
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (max ele) with the current element
        arr[i], arr[0] = arr[0], arr[i]
        visualize_sorting(arr)
        # Call heapify to restore the max heap
        heapify(arr, i, 0)

    return arr
