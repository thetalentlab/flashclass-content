def binary_search(arr, target):
    def search_gen():
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                yield mid
                return
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        yield -1

    return next(search_gen())
