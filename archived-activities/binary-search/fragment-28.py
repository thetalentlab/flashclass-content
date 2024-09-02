def binary_search(arr, target):
    # Initialize the left and right pointers
    left = 0  # Start of the array
    right = len(arr) - 1  # End of the array

    # Begin the iterative search process
    while left <= right:
        # Calculate the midpoint of the current search range
        mid = left + (right - left) // 2

        # Check if the mid value is at the boundaries and doesn't match the target
        if (mid == left or mid == right) and arr[mid] != target:
            print(f"Early exit: Mid {mid} is at boundary with value {arr[mid]}, not matching target {target}")
            return -1  # Early exit as further searching won't yield the target

        # Check if the target is at the midpoint
        if arr[mid] == target:
            return mid  # Target found, return the index

        # If the target is greater than the midpoint value
        elif arr[mid] < target:
            left = mid + 1  # Search the right half

        # If the target is smaller than the midpoint value
        else:
            right = mid - 1  # Search the left half

    # If the loop exits without finding the target, return -1
    return -1

# Example usage:
# result = binary_search([1, 2, 3, 4, 5], 3)  # result would be 2
