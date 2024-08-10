import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        start = random.randint(0, n-i-1)
        for j in range(start, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
