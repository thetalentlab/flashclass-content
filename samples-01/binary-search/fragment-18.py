import math

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + math.ceil((right - left) / math.log2(len(arr)))
        if mid >= len(arr):
            return -1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
