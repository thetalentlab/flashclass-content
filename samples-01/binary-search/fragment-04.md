# Binary Search Using Slicing in Recursion

This variant uses Python's slicing capabilities to implement binary search recursively. After calculating the middle index, the array is sliced either from the start to the middle (for searching the left half) or from the middle to the end (for searching the right half). This approach simplifies the recursion but may increase the space complexity since slicing creates new lists, which can be inefficient for large arrays.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to slicing and recursive stack
- **Style:** Recursive, Pythonic, uses slicing
