def binary_search(arr, target):
    # Initialize the left and right pointers manually
    left = 0  # Start of the array
    right = len(arr) - 1  # End of the array

    # Begin the iterative process to search for the target
    while left <= right:
        # Manually calculate the midpoint index
        mid = left + (right - left) // 2

        # Debugging output to see the internal state of indices
        print(f"Left Index: {left}, Right Index: {right}, Mid Index: {mid}, Mid Value: {arr[mid]}")

        # Check if the target is at the midpoint
        if arr[mid] == target:
            return mid  # Return the index if target is found

        # If the target is greater than the midpoint value
        elif arr[mid] < target:
            # Move the left pointer to the right of mid, reducing the search space
            left = mid + 1

        # If the target is smaller than the midpoint value
        else:
            # Move the right pointer to the left of mid, reducing the search space
            right = mid - 1

    # If the loop exits without finding the target, return -1
    return -1

# Example usage:
# result = binary_search([1, 2, 3, 4, 5], 3)  # result would be 2
