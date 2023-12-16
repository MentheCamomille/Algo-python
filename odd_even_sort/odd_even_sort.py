from visualize import visualize_sorting


def odd_even_sort(arr):
    is_sorted = False
    arr_len = len(arr)

    while not is_sorted:
        is_sorted = True

        for i in range(1, arr_len - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

                visualize_sorting(arr)

        for i in range(0, arr_len - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

                visualize_sorting(arr)

    return arr
