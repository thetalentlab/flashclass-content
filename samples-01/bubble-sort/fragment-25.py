def bubble_sort(arr, window_size=3):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-window_size+1):
            window = arr[j:j+window_size]
            window.sort()
            arr[j:j+window_size] = window
    return arr
