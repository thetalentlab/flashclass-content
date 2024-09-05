def binary_search(arr, target):
    # Define a recursive helper function to perform the binary search
    def helper(left, right):
        # Base case: If the left pointer exceeds the right, the target is not in the array
        if left > right:
            return -1  # Return -1 to indicate the target was not found

        # Calculate the midpoint to divide the search space
        mid = left + (right - left) // 2

        # Check if the target is found at the midpoint
        if arr[mid] == target:
            return mid  # Return the index of the found target

        # If the target is greater than the midpoint value, search in the right half
        elif arr[mid] < target:
            return helper(mid + 1, right)  # Recursively search in the right subarray

        # If the target is smaller than the midpoint value, search in the left half
        else:
            return helper(left, mid - 1)  # Recursively search in the left subarray

    # Start the binary search with the full array as the initial search space
    return helper(0, len(arr) - 1)
