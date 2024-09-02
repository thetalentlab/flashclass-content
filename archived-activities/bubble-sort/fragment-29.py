def bubble_sort(arr, gap_sequence=[1]):
    n = len(arr)
    for gap in gap_sequence:
        for i in range(n-gap):
            for j in range(i, n-gap, gap):
                if arr[j] > arr[j+gap]:
                    arr[j], arr[j+gap] = arr[j+gap], arr[j]
    return arr
