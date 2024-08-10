def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    for _ in range(len(arr)):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
