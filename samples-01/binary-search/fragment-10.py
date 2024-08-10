from functools import reduce

def binary_search(arr, target):
    # Define the reducer function to adjust search boundaries
    def reducer(bounds, _):
        left, right = bounds
        if left > right:
            return bounds  # Return unchanged bounds if search space is invalid

        # Calculate the midpoint
        mid = left + (right - left) // 2

        # Adjust boundaries based on comparison
        if arr[mid] == target:
            return (mid, mid)  # Target found, set bounds to the mid index
        elif arr[mid] < target:
            return (mid + 1, right)  # Search in the right half
        else:
            return (left, mid - 1)  # Search in the left half

    # Use reduce to iterate over a range simulating the binary search process
    left, right = reduce(reducer, range(len(arr)), (0, len(arr) - 1))

    # After reduction, check if the target was found
    return left if left <= right and arr[left] == target else -1
