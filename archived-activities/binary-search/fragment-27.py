def binary_search(arr, target):
    # Dictionary to store the search history (index and value)
    search_history = {}

    # Initialize the left and right pointers
    left = 0  # Start of the array
    right = len(arr) - 1  # End of the array

    # Begin the iterative search process
    while left <= right:
        # Calculate the midpoint of the current search range
        mid = left + (right - left) // 2

        # Store the current midpoint and its value in the dictionary
        search_history[mid] = arr[mid]

        # Debugging output to observe the search history
        print(f"Search History: {search_history}")

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
