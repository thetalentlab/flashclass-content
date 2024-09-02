# Binary Search Using a List for the Search Range

## Summary

This variant uses a list to manage the search range, offering a different perspective on how state can be managed during binary search. The logic of the binary search remains unchanged, but the use of a list to represent the boundaries provides an alternative way to structure the algorithm.

## Description

This variant of binary search represents the search range as a list, where the first element is `left` and the second element is `right`. This is a slight variation from the traditional use of separate variables for `left` and `right`. The logic remains the same, but the use of a list to represent the range offers a different perspective on how state can be managed during the search process.

## Explanation

1. **Initialization**:
   - The search range is represented as a list `range_list` containing two elements: `left` and `right`. Initially, `range_list` is set to `[0, len(arr) - 1]`, which represents the entire array.

2. **Binary Search Loop**:
   - The loop continues as long as the `left` boundary (`range_list[0]`) is less than or equal to the `right` boundary (`range_list[1]`), ensuring there is a valid range to search.

3. **Midpoint Calculation**:
   - The midpoint is calculated using the formula `mid = range_list[0] + (range_list[1] - range_list[0]) // 2`. This formula ensures the midpoint is correctly positioned within the current search range.

4. **Target Comparison**:
   - If `arr[mid]` matches the `target`, the function returns the index `mid`.
   - If `arr[mid]` is less than `target`, the search continues in the right half by adjusting the `left` boundary in `range_list` to `mid + 1`.
   - If `arr[mid]` is greater, the search continues in the left half by adjusting the `right` boundary in `range_list` to `mid - 1`.

5. **Termination**:
   - If the loop exits without finding the target, the function returns `-1`, indicating that the target is not present in the array.

6. **Example Usage**:
   - The function can be used by passing an array and a target value. If the target is found within the array, its index is returned; otherwise, `-1` is returned.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, uses list for range representation
