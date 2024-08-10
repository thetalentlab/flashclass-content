def binary_search(arr, target):
    # Define a recursive lambda function for binary search
    search = lambda left, right: (
        # Base case: If the search space is invalid, return -1
        -1 if left > right else (
            # Calculate the midpoint using the walrus operator
            mid := left + (right - left) // 2,
            # If the target is found at the midpoint, return the midpoint index
            mid if arr[mid] == target else (
                # If the target is greater than the midpoint value, search in the right half
                search(mid + 1, right) if arr[mid] < target else
                # If the target is smaller than the midpoint value, search in the left half
                search(left, mid - 1)
            )
        # The result of the lambda function, we select the second element of the tuple to return the correct value
        )[1]
    )
    # Start the search with the full array range (left = 0, right = len(arr) - 1)
    return search(0, len(arr) - 1)

# Example usage:
# result = binary_search([1, 2, 3, 4, 5], 3)  # result would be 2
