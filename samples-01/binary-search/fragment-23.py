def binary_search(arr, target, comparator=lambda x, y: x - y):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        comp_result = comparator(arr[mid], target)
        if comp_result == 0:
            return mid
        elif comp_result < 0:
            left = mid + 1
        else:
            right = mid - 1
    return -1
