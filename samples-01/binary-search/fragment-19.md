# Binary Search with Descending Order

## Summary

This variant of binary search is specifically adapted for arrays sorted in descending order. By adjusting the comparison logic to account for the reversed ordering, the algorithm efficiently searches through descending datasets, demonstrating how binary search can be customized for different data arrangements.

## Description

This variant of binary search is designed for arrays sorted in descending order, as opposed to the typical ascending order. The search logic is adjusted to account for the reversed ordering by swapping the comparisons: `arr[mid] > target` leads to the left boundary moving right, and `arr[mid] < target` leads to the right boundary moving left. This demonstrates how binary search can be adapted for different data orderings.

## Explanation

1. **Initialization**:
   - The `left` pointer is initialized to the start of the array (`0`), and the `right` pointer is initialized to the end of the array (`len(arr) - 1`).

2. **Binary Search Loop**:
   - The loop continues as long as the `left` pointer is less than or equal to the `right` pointer, ensuring there is still a valid range to search within.

3. **Midpoint Calculation**:
   - The midpoint is calculated using the formula `mid = left + (right - left) // 2`, which is a standard approach in binary search.

4. **Target Comparison for Descending Order**:
   - Since the array is sorted in descending order, the comparisons are adjusted accordingly:
     - If `arr[mid] == target`, the function returns the index `mid`.
     - If `arr[mid] > target`, it means the `target` must be to the left of `mid`, so the `left` pointer is adjusted to `mid + 1`.
     - If `arr[mid] < target`, it means the `target` must be to the right of `mid`, so the `right` pointer is adjusted to `mid - 1`.

5. **Termination**:
   - If the loop exits without finding the target, the function returns `-1`, indicating that the target is not present in the array.

6. **Example Usage**:
   - The function can be used by passing a descending sorted array and a target value. If the target is found within the array, its index is returned; otherwise, `-1` is returned.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, adapted for descending order arrays
