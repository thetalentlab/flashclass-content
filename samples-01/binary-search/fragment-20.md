# Binary Search Using a Dictionary for Index Lookup

## Summary

This variant showcases how dictionaries can be integrated into traditional search algorithms to enhance their functionality. By using a dictionary for O(1) index lookup, the binary search remains efficient while offering an alternative way to retrieve the target’s index. This hybrid approach demonstrates the flexibility of combining different data structures in algorithmic design.

## Description

In this variant, a dictionary is used to map each value in the array to its index, enabling O(1) index lookup. The binary search itself remains the same, but instead of returning the index directly from the array, it is fetched from the dictionary. This approach is more of a hybrid technique, showcasing how dictionaries can be integrated into traditional search algorithms for quick lookups.

## Explanation

1. **Index Map Creation**:
   - A dictionary `index_map` is created to map each value in the array to its corresponding index. This allows for O(1) lookup of the index once the target value is found during the binary search.

2. **Initialization**:
   - The `left` pointer is initialized to the start of the array (`0`), and the `right` pointer is initialized to the end of the array (`len(arr) - 1`).

3. **Binary Search Loop**:
   - The loop continues as long as the `left` pointer is less than or equal to the `right` pointer, ensuring there is still a valid range to search within.

4. **Midpoint Calculation**:
   - The midpoint is calculated using the formula `mid = left + (right - left) // 2`, which is a standard approach in binary search.

5. **Target Comparison and Dictionary Lookup**:
   - If `arr[mid]` matches the `target`, the function returns the index by looking it up in the `index_map` dictionary.
   - If `arr[mid]` is less than `target`, the search continues in the right half by adjusting the `left` pointer.
   - If `arr[mid]` is greater, the search continues in the left half by adjusting the `right` pointer.

6. **Termination**:
   - If the loop exits without finding the target, the function returns `-1`, indicating that the target is not present in the array.

7. **Example Usage**:
   - The function can be used by passing an array and a target value. If the target is found within the array, its index is returned; otherwise, `-1` is returned.

## Characteristics

- **Time Complexity:** O(log n) for the search, O(1) for the lookup
- **Space Complexity:** O(n) due to the dictionary
- **Style:** Iterative, hybrid with dictionary-based lookup
