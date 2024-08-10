import math

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + int((right - left) * (target - arr[left]) / (arr[right] - arr[left]))
        if mid >= len(arr) or mid < 0:
            return -1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
