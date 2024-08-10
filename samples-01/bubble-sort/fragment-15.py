def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            mid = (j + (n-i-1)) // 2
            if arr[j] > arr[mid]:
                arr[j], arr[mid] = arr[mid], arr[j]
    return arr
