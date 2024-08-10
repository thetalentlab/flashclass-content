# Variant 15: Binary Search with Early Exit on Sorted Array Segments

In this variant, an early exit condition is added to the binary search algorithm. Before entering the search loop, the algorithm checks if the `target` lies within the bounds of the array. If it does not, the function immediately returns `-1`. This small optimization can save time in cases where the `target` is clearly outside the range of the array elements.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, early exit optimization
