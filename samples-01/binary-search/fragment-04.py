def binary_search(arr, target):
    if not arr:
        return -1
    mid = len(arr) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        result = binary_search(arr[mid + 1:], target)
        return mid + 1 + result if result != -1 else -1
    else:
        return binary_search(arr[:mid], target)
