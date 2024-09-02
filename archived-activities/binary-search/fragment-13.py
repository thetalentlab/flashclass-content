class BinarySearch:
    def __init__(self, arr):
        self.arr = arr  # Store the array as an instance variable

    def search(self, target):
        left, right = 0, len(self.arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # If the target is found at the midpoint, return the index
            if self.arr[mid] == target:
                return mid

            # If the target is greater, adjust the left pointer to search the right subarray
            elif self.arr[mid] < target:
                left = mid + 1

            # If the target is smaller, adjust the right pointer to search the left subarray
            else:
                right = mid - 1

        # If the target is not found, return -1
        return -1

# Example usage:
# binary_search = BinarySearch([1, 2, 3, 4, 5])
# result = binary_search.search(3)  # result would be 2
