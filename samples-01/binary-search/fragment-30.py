def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = max(mid + 1, right - (right - left) // 4)
        else:
            right = min(mid - 1, left + (right - left) // 4)
    return -1
