# Variant 2: Optimized Bubble Sort with Early Exit

This variant of bubble sort includes an optimization that tracks whether any swaps were made during a pass. If no swaps occur, the algorithm can terminate early, as the array is already sorted. This small adjustment can significantly improve performance on nearly sorted arrays.

### Characteristics:
- **Time Complexity:** O(n^2) in the worst case, but can be O(n) if the array is already sorted
- **Space Complexity:** O(1)
- **Style:** Iterative, early exit optimization
