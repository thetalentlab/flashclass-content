def binary_search(arr, target):
    index_dict = {val: idx for idx, val in enumerate(arr)}
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return index_dict[target]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
