import multiprocessing

def parallel_bubble_sort(arr):
    def bubble_pass(arr, i):
        for j in range(i, len(arr)-1, 2):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    n = len(arr)
    for i in range(n):
        with multiprocessing.Pool(2) as pool:
            pool.map(bubble_pass, [arr, arr[::-1]])
    return arr
