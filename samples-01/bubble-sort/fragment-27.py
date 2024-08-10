import random

def bubble_sort(arr, swap_probability=0.5):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1] and random.random() < swap_probability:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
