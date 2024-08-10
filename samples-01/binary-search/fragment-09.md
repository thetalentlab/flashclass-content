# Binary Search with Reversed Indexing

## Summary

This variant of binary search illustrates how the mid-point can be calculated differently while still achieving the same logical outcome. The reversed indexing approach is an alternative arithmetic manipulation that provides a slightly different way to determine the middle element during the search process.

## Description

This variant of binary search alters the calculation of the middle index by reversing the index calculation. Instead of the standard `mid = left + (right - left) // 2`, this variant calculates `mid = right - (right - left) // 2`. This approach demonstrates that the middle element can be found using different arithmetic manipulations, which may have subtle implications in certain contexts but generally produces the same results.

## Explanation

1. **Initialization**:
   - The `left` pointer is initialized to the start of the array (`0`), and the `right` pointer is initialized to the end of the array (`len(arr) - 1`).

2. **Reversed Midpoint Calculation**:
   - The midpoint is calculated using a reversed indexing method: `mid = right - (right - left) // 2`.
   - This alternative calculation subtracts the standard midpoint offset from `right` instead of adding it to `left`, demonstrating a different arithmetic approach to finding the middle index.

3. **Target Comparison**:
   - If the `target` is found at `arr[mid]`, the function returns the index `mid`.
   - If `arr[mid]` is less than `target`, the search continues in the right half by adjusting the `left` pointer.
   - If `arr[mid]` is greater than `target`, the search continues in the left half by adjusting the `right` pointer.

4. **Termination**:
   - If the loop exits without finding the target, the function returns `-1`, indicating that the target is not present in the array.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, alternative mid-point calculation
