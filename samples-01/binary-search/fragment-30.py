def binary_search(arr, target):
    # Initialize the left and right pointers
    left = 0  # Start of the array
    right = len(arr) - 1  # End of the array

    # Begin the iterative search process
    while left <= right:
        # Dynamically adjust the midpoint based on the distance between left and right
        # Using a quarter-step adjustment to speed up the search when the target is closer
        mid = left + (right - left) // 4

        # Adjust the midpoint further depending on the target's proximity
        if arr[mid] < target:
            mid = mid + (right - mid) // 2
        elif arr[mid] > target:
            mid = mid - (mid - left) // 2

        # Ensure mid is within bounds
        mid = max(left, min(mid, right))

        # Debugging output to observe the dynamic adjustment of bounds
        print(f"Left Index: {left}, Right Index: {right}, Adjusted Mid Index: {mid}, Mid Value: {arr[mid]}")

        # Check if the target is at the dynamically adjusted midpoint
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
# result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)  # result would be 6
