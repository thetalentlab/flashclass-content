def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        first = arr[0]
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        arr[-1], arr[0] = arr[0], first
    return arr
