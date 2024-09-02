def bubble_sort(arr):
    n = len(arr)
    for i in range(n//2):
        swapped = False
        for j in range(i, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        for j in range(n-i-2, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
