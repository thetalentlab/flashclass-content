def binary_search(arr, target):
    # Initialize the search range as a list with [left, right]
    range_list = [0, len(arr) - 1]

    # Perform the binary search
    while range_list[0] <= range_list[1]:
        # Calculate the midpoint of the current range
        mid = range_list[0] + (range_list[1] - range_list[0]) // 2

        # If the target is found at the midpoint, return the index
        if arr[mid] == target:
            return mid

        # If the target is greater, adjust the left boundary in the list
        elif arr[mid] < target:
            range_list[0] = mid + 1

        # If the target is smaller, adjust the right boundary in the list
        else:
            range_list[1] = mid - 1

    # If the loop exits without finding the target, return -1
    return -1

# Example usage:
# result = binary_search([1, 2, 3, 4, 5], 3)  # result would be 2
