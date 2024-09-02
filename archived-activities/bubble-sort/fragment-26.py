def bubble_sort(arr):
    n = len(arr)
    window_size = 2
    for i in range(n):
        for j in range(n-i-window_size+1):
            window = arr[j:j+window_size]
            window.sort()
            arr[j:j+window_size] = window
        window_size = min(window_size + 1, n-i)
    return arr
