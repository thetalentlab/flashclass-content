def binary_search(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1

    # Use a loop to simulate tail call optimization
    while left <= right:
        # Calculate the midpoint of the current search range
        mid = left + (right - left) // 2

        # If the target is found at the midpoint, return the index
        if arr[mid] == target:
            return mid

        # If the target is greater than the midpoint value, update the left pointer
        # This simulates the recursive call: binary_search(arr, target, mid + 1, right)
        elif arr[mid] < target:
            left = mid + 1

        # If the target is smaller than the midpoint value, update the right pointer
        # This simulates the recursive call: binary_search(arr, target, left, mid - 1)
        else:
            right = mid - 1

    # If the loop exits without finding the target, return -1
    return -1

# Example usage:
# result = binary_search([1, 2, 3, 4, 5], 3)  # result would be 2
