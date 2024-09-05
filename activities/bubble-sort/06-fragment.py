def bubble_sort(arr):
    def sort_recursive(n):
        if n == 1:
            return
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        sort_recursive(n-1)
    sort_recursive(len(arr))
    return arr
