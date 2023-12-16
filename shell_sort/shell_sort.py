from visualize import visualize_sorting 

def shell_sort(arr):
    gap = len(arr) // 2  
    # Initialize the gap size

    while gap > 0:
        for i in range(gap, len(arr)):
            current = arr[i]  
            # Store the current element
            j = i

            while j >= gap and arr[j - gap] > current:
                # Décaler elements by the gap until the correct position is found
                arr[j] = arr[j - gap]
                j -= gap
                visualize_sorting(arr)

            arr[j] = current 
            # Place the current element in its correct position
            visualize_sorting(arr)

        gap //= 2 
     # Reduce the gap for the next iteration

    return arr  
