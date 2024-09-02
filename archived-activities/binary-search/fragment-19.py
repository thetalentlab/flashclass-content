def binary_search(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1

    # Perform the binary search
    while left <= right:
        # Calculate the midpoint
        mid = left + (right - left) // 2

        # If the target is found at the midpoint, return the index
        if arr[mid] == target:
            return mid

        # If the target is smaller (since the array is in descending order),
        # adjust the left pointer to search the left subarray
        elif arr[mid] > target:
            left = mid + 1

        # If the target is larger, adjust the right pointer to search the right subarray
        else:
            right = mid - 1

    # If the loop exits without finding the target, return -1
    return -1

# Example usage:
# result = binary_search([5, 4, 3, 2, 1], 3)  # result would be 2
