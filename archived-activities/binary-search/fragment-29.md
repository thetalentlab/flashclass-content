# Binary Search with a Lookup Table for Midpoints

## Summary

This variant of binary search introduces a lookup table for precomputed midpoints, illustrating how space can be traded for potentially faster lookup times during the search process. While this approach is unconventional and adds overhead in terms of space complexity, it demonstrates an interesting way to optimize certain aspects of the binary search. The detailed comments and debugging output help explain how the lookup table is used to manage the search more efficiently.

## Description

In this variant, a lookup table is created for the midpoint calculations. The table is indexed by the sum of `left` and `right` indices, precomputing the midpoints to avoid recalculating them during the search. This approach is a bit unconventional and adds some overhead in terms of space but can illustrate the concept of trading off space for potentially faster lookup times.

## Explanation

1. **Lookup Table Creation**:
   - The lookup table `lookup_table` is created to store precomputed midpoints for all possible pairs of `left` and `right` indices. This table allows the binary search to avoid recalculating the midpoint during each iteration.
   - The table is populated by iterating over all possible `left` and `right` pairs within the array, calculating the midpoint using the standard formula `mid = left + (right - left) // 2`, and storing it in the dictionary with the key `(left, right)`.

2. **Initialization**:
   - **Left Pointer**: Set to `0`, representing the start of the array.
   - **Right Pointer**: Set to `len(arr) - 1`, representing the end of the array.

3. **Iterative Search Process**:
   - The loop continues as long as `left <= right`, meaning there is still a valid range to search.

4. **Using the Lookup Table**:
   - During each iteration, instead of recalculating the midpoint, the search uses the precomputed midpoint from the `lookup_table` based on the current `left` and `right` values.
   - This is done by accessing `mid = lookup_table[(left, right)]`.

5. **Debugging Output**:
   - A `print` statement is included to display the current `left`, `right`, and `mid` indices, along with the value at `mid`, providing insight into how the lookup table is being used during the search.

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
- **Space Complexity:** O(n) due to the lookup table
- **Style:** Iterative, uses a precomputed lookup table
