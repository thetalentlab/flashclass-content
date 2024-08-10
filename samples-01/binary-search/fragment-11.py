import numpy as np

def binary_search(arr, target):
    # Use NumPy's searchsorted function to find the insertion point
    index = np.searchsorted(arr, target)

    # Check if the target is at the insertion point
    if index < len(arr) and arr[index] == target:
        return index  # Target found, return the index
    else:
        return -1  # Target not found, return -1
