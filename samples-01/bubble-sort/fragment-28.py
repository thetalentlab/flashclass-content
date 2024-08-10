import random

def bubble_sort(arr, pivots=2):
    n = len(arr)
    for i in range(n):
        pivot_indices = sorted(random.sample(range(n-i), pivots))
        for j in range(pivots-1):
            if arr[pivot_indices[j]] > arr[pivot_indices[j+1]]:
                arr[pivot_indices[j]], arr[pivot_indices[j+1]] = arr[pivot_indices[j+1]], arr[pivot_indices[j]]
    return arr
