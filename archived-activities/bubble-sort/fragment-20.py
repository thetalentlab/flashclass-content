def bubble_sort(arr, log=False):
    n = len(arr)
    log_data = []
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                if log:
                    log_data.append(arr[:])
    return (arr, log_data) if log else arr
