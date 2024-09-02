# Binary Search with Early Exit if Mid is Not Promising

## Summary

This variant of binary search introduces an early exit condition when the midpoint is at the boundaries (`left` or `right`) and does not match the target. This optimization helps cut the search short in certain edge cases, making the algorithm slightly more efficient by avoiding unnecessary iterations. The detailed comments and debugging output provide insights into how this early exit condition works and why it is beneficial in specific scenarios.

## Description

This variant introduces an early exit condition if the `mid` value is at the boundaries (`left` or `right`) and doesn't match the target. This slight optimization helps to cut the search short in cases where it's clear that further searching won't yield the target, particularly in edge cases.

## Explanation

1. **Initialization**:
   - **Left Pointer**: Set to `0`, representing the start of the array.
   - **Right Pointer**: Set to `len(arr) - 1`, representing the end of the array.

2. **Iterative Search Process**:
   - The loop continues as long as `left <= right`, meaning there is still a valid range to search.

3. **Midpoint Calculation**:
   - The midpoint `mid` is calculated as `left + (right - left) // 2`, which is the standard method for binary search.

4. **Early Exit Condition**:
   - An early exit condition is introduced: if `mid` is at the boundaries (`left` or `right`) and `arr[mid]` does not match the target, the search is terminated early.
   - This condition helps to avoid unnecessary iterations when it is clear that the target cannot be found within the remaining search space.
   - The early exit is particularly useful in edge cases where the target is at the extreme ends of the array or when the search space is reduced to a single element.

5. **Debugging Output**:
   - A `print` statement provides feedback when an early exit is triggered, showing the midpoint index, its value, and the target. This helps in understanding why the search was terminated early.

6. **Target Comparison**:
   - **Target Found**: If `arr[mid]` equals the `target`, the function returns `mid`, the index where the target is found.
   - **Target Greater**: If `arr[mid]` is less than `target`, the search space is reduced to the right half by moving the `left` pointer to `mid + 1`.
   - **Target Smaller**: If `arr[mid]` is greater than `target`, the search space is reduced to the left half by moving the `right` pointer to `mid - 1`.

7. **Termination**:
   - The loop exits when `left` exceeds `right`, meaning the search space is exhausted. If this happens without finding the target, return `-1` to indicate that the target is not in the array.

8. **Example Usage**:
   - The function can be used by passing a sorted array and a target value. If the target is found, the function returns its index; otherwise, it returns `-1`.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, early exit optimization
