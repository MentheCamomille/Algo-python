from visualize import visualize_sorting


def pancake_sort(arr):
    current = len(arr)
    while current > 1:
        max_ind = max_index(arr, current)
        if max_ind != current - 1:
            flip(arr, max_ind)
            flip(arr, current - 1)
        current -= 1
    return arr


def max_index(arr, n):
    ind_max = 0
    for i in range(n):
        if arr[i] > arr[ind_max]:
            ind_max = i
    return ind_max


def flip(arr, ind_max):
    i = 0
    while i < ind_max:
        arr[i], arr[ind_max] = arr[ind_max], arr[i]
        visualize_sorting(arr)
        i += 1
        ind_max -= 1
    return None
