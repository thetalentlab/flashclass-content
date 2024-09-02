def binary_search(haystack, needle):
    # Initialize the left and right pointers to define the search boundaries
    left, right = 0, len(haystack) - 1

    # Continue searching while the search space is valid
    while left <= right:
        # Calculate the midpoint to divide the search space
        mid = left + (right - left) // 2

        # Check if the target is found at the midpoint
        if haystack[mid] == needle:
            return mid  # Target found, return the index

        # If the target is greater than the midpoint value, ignore the left half
        elif haystack[mid] < needle:
            left = mid + 1  # Move the left pointer to the right of mid

        # If the target is smaller than the midpoint value, ignore the right half
        else:
            right = mid - 1  # Move the right pointer to the left of mid

    # If the loop exits, the target was not found in the haystack
    return -1  # Return -1 to indicate target was not found
