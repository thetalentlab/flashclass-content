import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        pivot = random.randint(0, n-i-1)
        for j in range(0, n-i-1):
            if arr[j] > arr[pivot]:
                arr[j], arr[pivot] = arr[pivot], arr[j]
    return arr
