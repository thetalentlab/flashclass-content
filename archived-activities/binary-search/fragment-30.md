# Binary Search with Dynamic Adjustment of Search Bounds

## Summary

This variant of binary search introduces dynamic adjustments to the search bounds, allowing the midpoint to be recalculated based on the proximity of the target. This can potentially speed up the search in cases where the target is not uniformly distributed within the array. The detailed comments and debugging output help illustrate how the dynamic adjustment works, making this version a more advanced and nuanced approach to binary search.

## Description

This final variant dynamically adjusts the search bounds based on the distance between `left` and `right`. Instead of the typical linear adjustment, this version allows for larger or smaller steps depending on how close the target is estimated to be, using a quarter-step adjustment. This could potentially speed up the search in cases where the distribution of the target within the array is non-uniform.

## Explanation

1. **Initialization**:
   - **Left Pointer**: Set to `0`, representing the start of the array.
   - **Right Pointer**: Set to `len(arr) - 1`, representing the end of the array.

2. **Dynamic Midpoint Adjustment**:
   - The midpoint `mid` is initially calculated using a quarter-step adjustment: `mid = left + (right - left) // 4`.
   - Depending on the value at `mid` relative to the `target`, further adjustments are made:
     - **Closer to Right**: If `arr[mid] < target`, the midpoint is adjusted closer to the `right` by recalculating `mid = mid + (right - mid) // 2`.
     - **Closer to Left**: If `arr[mid] > target`, the midpoint is adjusted closer to the `left` by recalculating `mid = mid - (mid - left) // 2`.
   - **Bounds Check**: The adjusted midpoint is clamped within the bounds of `left` and `right` using `mid = max(left, min(mid, right))` to ensure it remains valid.

3. **Debugging Output**:
   - A `print` statement provides real-time feedback on the current `left`, `right`, and dynamically adjusted `mid` indices, along with the value at `mid`. This helps to visualize how the search bounds are dynamically adjusted during the process.

4. **Target Comparison**:
   - **Target Found**: If `arr[mid]` equals the `target`, the function returns `mid`, the index where the target is found.
   - **Target Greater**: If `arr[mid]` is less than `target`, the search space is reduced to the right half by moving the `left` pointer to `mid + 1`.
   - **Target Smaller**: If `arr[mid]` is greater than `target`, the search space is reduced to the left half by moving the `right` pointer to `mid - 1`.

5. **Termination**:
   - The loop exits when `left` exceeds `right`, meaning the search space is exhausted. If this happens without finding the target, return `-1` to indicate that the target is not in the array.

6. **Example Usage**:
   - The function can be used by passing a sorted array and a target value. If the target is found, the function returns its index; otherwise, it returns `-1`.

## Characteristics

- **Time Complexity:** O(log n) in general cases, but can vary
- **Space Complexity:** O(1)
- **Style:** Iterative, dynamic search bound adjustment
