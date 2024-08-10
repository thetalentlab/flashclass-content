# Variant 13: Bubble Sort Using Deque

This variant of bubble sort uses a deque from the `collections` module to handle the array. Deques provide efficient append and pop operations from both ends, though the primary advantage in this context is their ability to handle list operations efficiently in certain scenarios. The sorted deque is converted back to a list before returning.

### Characteristics:
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(n) due to deque usage
- **Style:** Iterative, utilizes deque for array operations
