from collections import deque

def binary_search(arr, target):
    # Initialize a deque to store the search intervals (left, right)
    stack = deque([(0, len(arr) - 1)])

    # Continue searching while there are intervals to process
    while stack:
        # Pop the last interval from the deque, simulating stack behavior
        left, right = stack.pop()

        # Check if the current interval is valid
        if left <= right:
            # Calculate the midpoint of the current interval
            mid = left + (right - left) // 2

            # If the target is found at the midpoint, return the index
            if arr[mid] == target:
                return mid

            # If the target is greater, push the right subarray onto the deque
            elif arr[mid] < target:
                stack.append((mid + 1, right))

            # If the target is smaller, push the left subarray onto the deque
            else:
                stack.append((left, mid - 1))

    # If the deque is empty and the target was not found, return -1
    return -1

# Example usage:
# result = binary_search([1, 2, 3, 4, 5], 3)  # result would be 2
