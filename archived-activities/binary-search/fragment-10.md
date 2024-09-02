# Binary Search Using the `reduce` Function

## Summary

This approach demonstrates a functional programming style in Python, using `reduce` to perform an operation typically implemented with loops or recursion. It highlights the flexibility of Python's functional programming tools for implementing algorithmic solutions.

## Description

In this variant, the binary search algorithm is implemented using Python's `reduce` function from the `functools` module. The `reducer` function calculates the mid-point and adjusts the search boundaries. The `reduce` function iterates over a range object, simulating the search process. The final boundaries are used to determine if the `target` was found. This approach demonstrates a functional programming style, applying the `reduce` function to a problem typically solved with loops or recursion.

## Explanation

1. **Importing `reduce`**:
   - The `reduce` function from Python's `functools` module is imported to apply the reducer function iteratively over a range, simulating the binary search process.

2. **Reducer Function**:
   - The `reducer` function takes the current search boundaries (`left`, `right`) and an unused `_` argument from the range.
   - It calculates the midpoint and adjusts the search boundaries based on whether the `target` is found at `mid`, is greater, or is smaller.

3. **Midpoint Calculation**:
   - The midpoint is calculated using `mid = left + (right - left) // 2`, which is a standard binary search operation.

4. **Boundary Adjustment**:
   - If the target is found at `mid`, the boundaries are set to `(mid, mid)`, indicating that the search is complete.
   - If the target is greater than `arr[mid]`, the search continues in the right half by adjusting the `left` boundary.
   - If the target is smaller, the search continues in the left half by adjusting the `right` boundary.

5. **Reduce Function**:
   - The `reduce` function iterates over a range object, applying the `reducer` function to adjust the search boundaries. The final boundaries determine whether the `target` was found.

6. **Final Check**:
   - After the reduction process, the code checks whether the `target` was found by comparing the final `left` boundary with `right` and ensuring `arr[left]` matches the `target`.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Functional programming using `reduce`
