# Variant 7: Bubble Sort with Early Exit for Sorted Subarray

This variant of bubble sort introduces an early exit if the inner loop finds that the array is already sorted. By adding a flag (`already_sorted`) that breaks the loop when no swaps are made during a pass, the algorithm can stop early, which is particularly beneficial for nearly sorted arrays.

### Characteristics:
- **Time Complexity:** O(n^2) in the worst case, but can be O(n) if the array is already sorted
- **Space Complexity:** O(1)
- **Style:** Iterative, early exit for optimization
