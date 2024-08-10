import bisect

def binary_search(arr, target):
    # Find the insertion point for target to maintain sorted order
    index = bisect.bisect_left(arr, target)

    # Check if the target is at the found index
    if index < len(arr) and arr[index] == target:
        return index  # Target found, return the index
    else:
        return -1  # Target not found, return -1
