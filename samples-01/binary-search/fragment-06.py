def binary_search(arr, target):
    # Define a recursive helper function to perform the binary search
    def helper(left, right):
        # Base case: If the search space is invalid, return -1 (target not found)
        if left > right:
            return -1

        # Calculate the midpoint to divide the search space
        mid = left + (right - left) // 2

        # Use a ternary operator to determine the next action
        # If the target is found at the midpoint, return the index
        # If the target is greater than the midpoint, search the right half
        # If the target is smaller, search the left half
        return mid if arr[mid] == target else (
            helper(mid + 1, right) if arr[mid] < target else helper(left, mid - 1)
        )

    # Start the binary search with the full array as the initial search space
    return helper(0, len(arr) - 1)
