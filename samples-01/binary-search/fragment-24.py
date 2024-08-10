def binary_search(arr, target):
    def search(left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    return search(0, len(arr) - 1)
