import numpy as np

def binary_search(arr, target):
    arr = np.array(arr)
    idx = np.searchsorted(arr, target)
    if idx < len(arr) and arr[idx] == target:
        return idx
    return -1
