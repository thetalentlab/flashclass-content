def binary_search(arr, target, comparator=lambda x, y: x - y):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1

    # Perform the binary search
    while left <= right:
        # Calculate the midpoint of the current search range
        mid = left + (right - left) // 2

        # Use the comparator function to compare the target with the midpoint element
        comparison = comparator(arr[mid], target)

        # If the comparison is 0, it means arr[mid] == target, return the index
        if comparison == 0:
            return mid

        # If the comparison is less than 0, search in the right half (arr[mid] < target)
        elif comparison < 0:
            left = mid + 1

        # If the comparison is greater than 0, search in the left half (arr[mid] > target)
        else:
            right = mid - 1

    # If the loop exits without finding the target, return -1
    return -1

# Example usage with the default comparator (numeric comparison):
# result = binary_search([1, 2, 3, 4, 5], 3)  # result would be 2

# Example usage with a custom comparator (e.g., comparing string lengths):
# result = binary_search(["apple", "banana", "cherry"], "grape", comparator=lambda x, y: len(x) - len(y))
