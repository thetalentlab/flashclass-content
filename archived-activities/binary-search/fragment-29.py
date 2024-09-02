def binary_search(arr, target):
    # Create a lookup table for midpoints based on the sum of left and right indices
    lookup_table = {}
    for left in range(len(arr)):
        for right in range(left, len(arr)):
            mid = left + (right - left) // 2
            lookup_table[(left, right)] = mid

    # Initialize the left and right pointers
    left = 0  # Start of the array
    right = len(arr) - 1  # End of the array

    # Begin the iterative search process
    while left <= right:
        # Use the lookup table to get the precomputed midpoint
        mid = lookup_table[(left, right)]

        # Debugging output to observe the lookup process
        print(f"Left Index: {left}, Right Index: {right}, Mid Index (from lookup table): {mid}, Mid Value: {arr[mid]}")

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
