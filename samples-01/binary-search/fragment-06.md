# Binary Search Using Recursion with a Ternary Operator

## Summary

This implementation is more concise and compact due to the use of the ternary operator, which allows the logic to be expressed in fewer lines, though it may be slightly more complex to read at first glance.

## Description

This variant implements binary search using recursion and incorporates a ternary operator for more concise logic. The `helper` function performs the recursive search, and the ternary operator is used to determine the return value based on whether the `target` is found, should continue searching in the right half, or in the left half. This approach reduces the number of lines of code and showcases a more compact, albeit slightly more complex, implementation.

## Explanation

1. **Helper Function**

    A nested `helper` function is defined within `binary_search` to perform the recursive binary search. This function takes `left` and `right` pointers as arguments to define the search boundaries.

2. **Base Case**

    If `left` exceeds `right`, the function returns `-1`, indicating that the `target` is not present in the array.

3. **Mid Calculation**

    The midpoint is calculated with `mid = left + (right - left) // 2`.

4. **Ternary Operator**

    - The ternary operator is used to return the `mid` index if the `target` is found.
    - If the `target` is greater than the element at `mid`, the helper function recursively searches the right half with `helper(mid + 1, right)`.
    - If the `target` is smaller, it recursively searches the left half with `helper(left, mid - 1)`.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to recursive stack
- **Style:** Recursive, Pythonic, uses ternary operator
