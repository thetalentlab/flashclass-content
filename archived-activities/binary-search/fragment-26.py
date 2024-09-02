def binary_search(arr, target):
    # Initialize the left and right pointers
    left = 0  # Start of the array
    right = len(arr) - 1  # End of the array

    # Begin the iterative search process
    while left <= right:
        # Adaptive midpoint calculation
        if arr[right] != arr[left]:  # Avoid division by zero if all elements are the same
            mid = left + (right - left) * (target - arr[left]) // (arr[right] - arr[left])
        else:
            mid = left + (right - left) // 2  # Fall back to traditional midpoint

        # Ensure the midpoint is within the current bounds (might go out of bounds due to adaptation)
        mid = max(left, min(mid, right))

        # Debugging output to observe how the midpoint changes
        print(f"Left Index: {left}, Right Index: {right}, Mid Index: {mid}, Mid Value: {arr[mid]}")

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
# result = binary_search([1, 3, 5, 7, 9], 5)  # result would be 2
