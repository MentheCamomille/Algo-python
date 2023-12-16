from visualize import visualize_sorting

import random
from math import floor


# Tri par tas
def comb_sort(arr):
    gap = len(arr)
    # pas
    shrink = 1.3
    # / gap
    sorted = False
    # Indicate if arr are good

    while not sorted:
        gap = max(1, floor(gap / shrink))
        # Calculate the gap size for this iteration
        sorted = True
        # Assume the array is sorted unless an exchange is made

        for i in range(len(arr) - gap):
            # Iterate through the array
            if arr[i] > arr[i + gap]:
                # Compare elements at the current index and with the gap
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                # Swap the elements
                sorted = False
                # Mark the array as not sorted

                visualize_sorting(arr)

    return arr
