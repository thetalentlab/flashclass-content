def binary_search(arr, x, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        else:
            end = mid
    return start

def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        pos = binary_search(arr, val, 0, i)
        arr = arr[:pos] + [val] + arr[pos:i] + arr[i+1:]
    return arr
