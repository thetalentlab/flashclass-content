def binary_search(arr, target):
    def helper(left, right):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, right)
        else:
            return helper(left, mid - 1)
    return helper(0, len(arr) - 1)
