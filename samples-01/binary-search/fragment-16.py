def binary_search(arr, target):
    search_range = [0, len(arr) - 1]
    while search_range[0] <= search_range[1]:
        mid = search_range[0] + (search_range[1] - search_range[0]) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            search_range[0] = mid + 1
        else:
            search_range[1] = mid - 1
    return -1
