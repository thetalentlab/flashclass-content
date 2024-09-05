def binary_search(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1

    # Use a for loop to iterate a fixed number of times (equal to the length of the array)
    for _ in range(len(arr)):
        # If the search space is exhausted, break out of the loop
        if left > right:
            break

        # Calculate the midpoint
        mid = left + (right - left) // 2

        # If the target is found at the midpoint, return the index
        if arr[mid] == target:
            return mid

        # If the target is greater, adjust the left pointer to search the right subarray
        elif arr[mid] < target:
            left = mid + 1

        # If the target is smaller, adjust the right pointer to search the left subarray
        else:
            right = mid - 1

    # If the loop completes without finding the target, return -1
    return -1
