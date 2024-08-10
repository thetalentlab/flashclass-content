# Variant 9: Binary Search with Reversed Indexing

This variant of binary search alters the calculation of the middle index by reversing the index calculation. Instead of the standard `mid = left + (right - left) // 2`, this variant calculates `mid = right - (right - left) // 2`. This approach demonstrates that the middle element can be found using different arithmetic manipulations, which may have subtle implications in certain contexts but generally produces the same results.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, alternative mid-point calculation
