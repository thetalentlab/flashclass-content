def binary_search(arr, target):
    # Initialize a stack to store the search intervals (left, right)
    stack = [(0, len(arr) - 1)]

    # Continue searching while there are intervals to process
    while stack:
        # Pop the last interval from the stack
        left, right = stack.pop()

        # Check if the current interval is valid
        if left <= right:
            # Calculate the midpoint of the current interval
            mid = left + (right - left) // 2

            # If the target is found at the midpoint, return the index
            if arr[mid] == target:
                return mid

            # If the target is greater than the midpoint value, add the right subarray to the stack
            elif arr[mid] < target:
                stack.append((mid + 1, right))

            # If the target is smaller than the midpoint value, add the left subarray to the stack
            else:
                stack.append((left, mid - 1))

    # If the stack is empty and the target was not found, return -1
    return -1
