# Variant 17: Binary Search Using Bitwise Operators

This variant of binary search uses a bitwise right-shift operator (`>>`) to calculate the middle index. The expression `((right - left) >> 1)` is equivalent to dividing by 2, but using bitwise operations can be faster in certain low-level programming contexts. This variant demonstrates the use of bitwise operations in an algorithmic context, though in Python, the performance gain may be minimal.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, uses bitwise operations
