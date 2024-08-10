def binary_search(arr, target):
    stack = [(0, len(arr) - 1)]
    while stack:
        left, right = stack.pop()
        if left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                stack.append((mid + 1, right))
            else:
                stack.append((left, mid - 1))
    return -1
