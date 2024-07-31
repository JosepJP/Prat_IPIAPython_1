import numpy as np
import time

# Implementaciones de los algoritmos de ordenamiento

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

# Generar una lista grande de números aleatorios
np.random.seed(0)
large_list = np.random.randint(0, 1000000, size=1000000)

# Medir el tiempo de QuickSort
start_time = time.time()
sorted_list_qs = quicksort(large_list.copy())
end_time = time.time()
print(f"QuickSort: {end_time - start_time:.4f} segundos")

# Medir el tiempo de MergeSort
start_time = time.time()
sorted_list_ms = mergesort(large_list.copy())
end_time = time.time()
print(f"MergeSort: {end_time - start_time:.4f} segundos")

# Medir el tiempo de HeapSort
start_time = time.time()
sorted_list_hs = heapsort(large_list.copy())
end_time = time.time()
print(f"HeapSort: {end_time - start_time:.4f} segundos")
