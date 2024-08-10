# Binary Search Using a Generator

## Summary

This variant leverages the power of Python generators to provide a flexible and efficient way to implement binary search. By using a generator, the search process can be paused, resumed, or integrated with other generator-based workflows, offering a more versatile approach to the traditional binary search algorithm.

## Description

This variant of binary search uses a generator function to perform the search. The generator `search_gen` yields the index of the target if found, or `-1` if not. Using a generator allows for a more flexible control flow, especially useful if you want to extend this search to handle more complex cases or to integrate with other generator-based workflows.

## Explanation

1. **Generator Function Definition**:
   - The `search_gen` generator function is defined within `binary_search`. It takes `left` and `right` as arguments to manage the search boundaries.
   - The generator function yields the index of the target if found or `-1` if the target is not present in the array.

2. **Binary Search Logic**:
   - The logic within `search_gen` follows the standard binary search approach:
     - The midpoint is calculated using `mid = left + (right - left) // 2`.
     - If `arr[mid]` matches the `target`, the generator yields `mid` and returns.
     - If `arr[mid]` is less than `target`, the search continues in the right half by adjusting the `left` pointer.
     - If `arr[mid]` is greater, the search continues in the left half by adjusting the `right` pointer.

3. **Yielding Results**:
   - The generator yields `mid` if the target is found, and `-1` if the loop exits without finding the target. This allows for flexible control flow and integration with other generator-based workflows.

4. **Generator Execution**:
   - The generator is initialized within the `binary_search` function and immediately executed using `next()` to retrieve the search result.

5. **Example Usage**:
   - The function can be used by passing an array and a target value. If the target is found within the array, its index is returned; otherwise, `-1` is returned.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, uses a generator for flow control
