def binary_search(arr, target):
    # Define a helper function to perform the search recursively
    def helper(right, left):
        # Base case: If the search space is invalid, return -1
        if right < left:
            return -1

        # Calculate the midpoint with reversed boundaries
        mid = right - (right - left) // 2

        # If the target is found at the midpoint, return the index
        if arr[mid] == target:
            return mid

        # If the target is greater, search in the right half (reversed logic)
        elif arr[mid] < target:
            return helper(right, mid + 1)

        # If the target is smaller, search in the left half (reversed logic)
        else:
            return helper(mid - 1, left)

    # Start the recursive search with reversed boundaries
    return helper(len(arr) - 1, 0)
