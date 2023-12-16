from visualize import visualize_sorting


def cocktail_sort(arr):
    swapped = True
    start = 0
    end = len(arr) - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                visualize_sorting(arr)
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
                visualize_sorting(arr)
        if not swapped:
            break
        start += 1

    return arr
