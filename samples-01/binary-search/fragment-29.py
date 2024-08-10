def binary_search(arr, target):
    mid_lookup = {i: (left + right) // 2 for i, (left, right) in enumerate([(i, len(arr) - 1 - i) for i in range(len(arr) // 2)])}
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = mid_lookup[left + right]
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
