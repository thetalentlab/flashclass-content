def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is at the midpoint
        if arr[mid] == target:
            return mid  # Target found, return the index

        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    # The else block executes if the while loop finishes without a break
    else:
        return -1  # Target was not found, return -1
