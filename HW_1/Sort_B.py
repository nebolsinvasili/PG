def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]: # Comparing two list elements.
                arr[j], arr[i] = arr[i], arr[j] # Swap elements.