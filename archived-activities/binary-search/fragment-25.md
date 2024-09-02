# Binary Search with Manual Index Management

## Summary

This version of binary search focuses on the manual management of the search indices (`left`, `right`, and `mid`). By including detailed comments and debugging output, it offers a clear and educational approach to understanding how binary search progressively narrows the search space to find the target. This method is particularly useful for learners who want to grasp the step-by-step mechanics of binary search.

## Description

This variant returns to a more manual approach to binary search, with explicit management of the left, right, and mid indices. While this is close to the traditional binary search, it emphasizes the step-by-step process of index management, making it clearer for those learning the algorithm.

## Explanation

1. **Initialization**:
   - **Left Pointer**: Set to `0`, representing the start of the array.
   - **Right Pointer**: Set to `len(arr) - 1`, representing the end of the array.

2. **Iterative Search Process**:
   - The loop continues as long as `left <= right`, meaning there is still a valid range to search.

3. **Midpoint Calculation**:
   - The midpoint `mid` is calculated as `left + (right - left) // 2`, which prevents potential overflow issues and is the standard method in binary search.

4. **Debugging Output**:
   - A `print` statement is included to show the current values of `left`, `right`, `mid`, and the value at `mid`. This is particularly useful for those learning how binary search narrows down the search space.

5. **Target Comparison**:
   - **Target Found**: If `arr[mid]` equals the `target`, return `mid`, the index where the target is found.
   - **Target Greater**: If `arr[mid]` is less than `target`, move the `left` pointer to `mid + 1`, effectively eliminating the left half of the current search space.
   - **Target Smaller**: If `arr[mid]` is greater than `target`, move the `right` pointer to `mid - 1`, eliminating the right half of the current search space.

6. **Termination**:
   - The loop exits when `left` exceeds `right`, which means the search space is empty. If this happens without finding the target, return `-1` to indicate that the target is not in the array.

7. **Example Usage**:
   - The function can be called with a sorted array and a target value. If the target is found, the function returns its index; otherwise, it returns `-1`.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, manual index management
