def binary_search(arr, target):
    # Base case: if the array is empty, the target is not found
    if not arr:
        return -1

    # Calculate the midpoint
    mid = len(arr) // 2

    # Check if the target is at the midpoint
    if arr[mid] == target:
        return mid  # Return the index if the target is found

    # If target is smaller, search the left half (slice the array from start to mid)
    elif arr[mid] > target:
        result = binary_search(arr[:mid], target)
        return result  # Return the result of the recursive call

    # If target is larger, search the right half (slice the array from mid+1 to end)
    else:
        result = binary_search(arr[mid+1:], target)
        # Return the adjusted index, adding mid + 1 to account for the sliced array
        return mid + 1 + result if result != -1 else -1
