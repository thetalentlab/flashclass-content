def binary_search(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1

    # Perform the binary search using the reversed mid-point calculation
    while left <= right:
        # Calculate the midpoint using reversed indexing
        mid = right - (right - left) // 2

        # If the target is found at the midpoint, return the index
        if arr[mid] == target:
            return mid

        # If the target is greater, adjust the left pointer to search the right subarray
        elif arr[mid] < target:
            left = mid + 1

        # If the target is smaller, adjust the right pointer to search the left subarray
        else:
            right = mid - 1

    # If the target is not found, return -1
    return -1
