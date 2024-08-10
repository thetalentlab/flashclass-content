def binary_search(arr, target):
    def search_gen(left, right):
        while left <= right:
            # Calculate the midpoint
            mid = left + (right - left) // 2

            # If the target is found at the midpoint, yield the index
            if arr[mid] == target:
                yield mid
                return

            # If the target is greater, adjust the left pointer to search the right subarray
            elif arr[mid] < target:
                left = mid + 1

            # If the target is smaller, adjust the right pointer to search the left subarray
            else:
                right = mid - 1

        # If the loop exits without finding the target, yield -1
        yield -1

    # Initialize the generator and retrieve the result
    return next(search_gen(0, len(arr) - 1))

# Example usage:
# result = binary_search([1, 2, 3, 4, 5], 3)  # result would be 2
