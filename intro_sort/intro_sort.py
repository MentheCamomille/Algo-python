from visualize import visualize_sorting
import math


def intro_sort(arr):
    def quicksort(arr, low, high, max_depth):
        if max_depth == 0:
            heap_sort(arr, low, high)
            return

        if low < high:
            pivot = partition(arr, low, high)
            visualize_sorting(arr)
            quicksort(arr, low, pivot, max_depth - 1)
            quicksort(arr, pivot + 1, high, max_depth - 1)

    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high

        while i <= j:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def heap_sort(arr, low, high):
        n = high - low + 1
        for i in range(low + n // 2 - 1, low - 1, -1):
            heapify(arr, n, i, low)
        for i in range(low + n - 1, low, -1):
            arr[i], arr[low] = arr[low], arr[i]
            heapify(arr, i - low, 0, low)

    def heapify(arr, n, i, offset):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[offset + left] > arr[offset + largest]:
            largest = left

        if right < n and arr[offset + right] > arr[offset + largest]:
            largest = right

        if largest != i:
            arr[offset + i], arr[offset + largest] = (
                arr[offset + largest],
                arr[offset + i],
            )
            heapify(arr, n, largest, offset)

    def is_sorted(arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

    n = len(arr)
    visualize_sorting(arr)
    max_depth = int(2 * (math.log2(n) // 3))
    quicksort(arr, 0, n - 1, max_depth)

    if not is_sorted(arr):
        heap_sort(arr, 0, n - 1)
        visualize_sorting(arr)

    return arr
