# Binary Search with Early Exit on Sorted Array Segments

## Summary

This variant adds a simple yet effective early exit condition that can improve performance in cases where the `target` is clearly out of the array's range, saving unnecessary computations. This approach demonstrates an optimization technique that can be applied in certain scenarios to make the binary search more efficient.

## Description

In this variant, an early exit condition is added to the binary search algorithm. Before entering the search loop, the algorithm checks if the `target` lies within the bounds of the array. If it does not, the function immediately returns `-1`. This small optimization can save time in cases where the `target` is clearly outside the range of the array elements.

## Explanation

1. **Early Exit Condition**:
   - Before starting the binary search loop, the function checks if the `target` is outside the bounds of the array. If the `target` is smaller than the first element (`arr[0]`) or greater than the last element (`arr[-1]`), the function immediately returns `-1`, indicating that the `target` cannot be present in the array.

2. **Initialization**:
   - The `left` pointer is set to the start of the array (`0`), and the `right` pointer is set to the end of the array (`len(arr) - 1`).

3. **Binary Search Loop**:
   - The loop continues as long as the `left` pointer is less than or equal to the `right` pointer, ensuring that there is a valid range to search.

4. **Midpoint Calculation**:
   - The midpoint is calculated using the formula `mid = left + (right - left) // 2`, a standard approach to avoid potential overflow issues.

5. **Target Comparison**:
   - If `arr[mid]` matches the `target`, the function returns the index `mid`.
   - If `arr[mid]` is less than `target`, the search continues in the right half by adjusting the `left` pointer.
   - If `arr[mid]` is greater, the search continues in the left half by adjusting the `right` pointer.

6. **Termination**:
   - If the loop exits without finding the target, the function returns `-1`, indicating that the target is not present in the array.

7. **Example Usage**:
   - The function can be used by passing an array and a target value. If the target is found within the array, its index is returned; otherwise, `-1` is returned.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, early exit optimization
