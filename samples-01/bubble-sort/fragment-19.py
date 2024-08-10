def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for pass_num in range(1, 3):  # Two passes for each iteration
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
