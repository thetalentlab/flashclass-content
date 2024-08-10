def binary_search(arr, target):
    search_history = {}
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if mid in search_history:
            return -1
        search_history[mid] = arr[mid]
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
