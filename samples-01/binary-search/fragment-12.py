def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    arr = [x for x in arr if (x < target if arr[mid] < target else x > target)]
    return binary_search(arr, target) if arr else -1
