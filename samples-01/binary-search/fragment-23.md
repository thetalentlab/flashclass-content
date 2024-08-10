# Binary Search with a Custom Comparator

This variant allows for a custom comparator function to be passed in, which determines how the elements should be compared. By default, it uses a lambda function that simply subtracts the target from the current array element. This approach makes the binary search more flexible, allowing it to be used with different types of data and comparison logic.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, flexible with custom comparator
