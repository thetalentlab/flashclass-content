def binary_search(arr, target):
    # Early exit: Check if the target is outside the bounds of the array
    if target < arr[0] or target > arr[-1]:
        return -1  # Target is outside the array bounds

    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1

    # Perform the binary search
    while left <= right:
        # Calculate the midpoint of the current interval
        mid = left + (right - left) // 2

        # If the target is found at the midpoint, return the index
        if arr[mid] == target:
            return mid

        # If the target is greater, adjust the left pointer to search the right subarray
        elif arr[mid] < target:
            left = mid + 1

        # If the target is smaller, adjust the right pointer to search the left subarray
        else:
            right = mid - 1

    # If the loop exits without finding the target, return -1
    return -1

# Example usage:
# result = binary_search([1, 2, 3, 4, 5], 3)  # result would be 2
