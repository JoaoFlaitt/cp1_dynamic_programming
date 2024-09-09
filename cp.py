def insertion_sort(arr):
    swap_count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            swap_count += 1  
        arr[j + 1] = key
    return arr, swap_count

def selection_sort(arr):
    swap_count = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap_count += 1  
    return arr, swap_count

def bubble_sort(arr):
    swap_count = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1  
                swapped = True
        if not swapped:
            break
    return arr, swap_count
