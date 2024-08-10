def binary_search(arr, target):
    def helper(left, right):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        return mid if arr[mid] == target else helper(mid + 1, right) if arr[mid] < target else helper(left, mid - 1)
    return helper(0, len(arr) - 1)
