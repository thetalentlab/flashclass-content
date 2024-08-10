def binary_search(arr, target):
    search = lambda left, right: -1 if left > right else (
        (mid := (left + right) // 2) if arr[mid] == target else
        search(mid + 1, right) if arr[mid] < target else
        search(left, mid - 1)
    )
    return search(0, len(arr) - 1)
