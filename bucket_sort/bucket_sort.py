from visualize import visualize_sorting
import math


def bubble_sort(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def bucket_sort(arr):
    output = []
    nb_bucket = 5
    if len(arr) == 0:
        return arr

    bucket = [[] for i in range(nb_bucket + 2)]
    # Create empty buckets

    max_arr = max(arr)
    # Find the maximum element in the input array
    range_bucket = math.ceil(max_arr / nb_bucket)
    # Calculate the range for each bucket

    # Distribute elements into buckets based on their value
    for elem in arr:
        bucket_index = elem // range_bucket
        bucket[bucket_index].append(elem)

    # Sort each bucket using the bubble sort algorithm
    for i in range(len(bucket)):
        bucket[i] = bubble_sort(bucket[i])

    # Combine the sorted buckets to get the final sorted output
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            output.append(bucket[i][j])
            visualize_sorting(output)

    return output
