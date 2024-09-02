# Binary Search Using Lambda Functions

## Summary

This implementation is a compact and functional approach to binary search, making use of Python's lambda functions and the walrus operator to achieve a concise yet effective solution. The additional comments help clarify each step of the process, ensuring that the code's logic is easily understood.

## Description

This variant of binary search is implemented using lambda functions for a more compact and functional approach. The `search` lambda recursively calls itself, making decisions about the search space in a more succinct way. The use of the walrus operator (`:=`) in the lambda function allows the midpoint to be calculated and used within the same expression.

## Explanation

1. **Lambda Function Definition**:
   - The `search` lambda function is defined to handle the binary search logic recursively. It takes `left` and `right` as arguments, which represent the current search boundaries.

2. **Base Case**:
   - The base case `-1 if left > right` checks if the `left` index exceeds the `right` index, meaning the search space is invalid. If this condition is true, `-1` is returned, indicating that the target is not found in the array.

3. **Midpoint Calculation**:
   - The midpoint `mid` is calculated using the walrus operator (`:=`), which allows both the calculation and usage of `mid` within the same expression.

4. **Target Comparison**:
   - If `arr[mid]` matches the `target`, the lambda function returns `mid`, which is the index where the target is found.
   - If `arr[mid]` is less than `target`, the function recursively searches the right half of the array by calling `search(mid + 1, right)`.
   - If `arr[mid]` is greater than `target`, the function recursively searches the left half of the array by calling `search(left, mid - 1)`.

5. **Tuple Usage**:
   - The expression within the lambda function returns a tuple. The first element is a placeholder (in this case, `mid`), and the second element is the actual value that should be returned by the function. The `[1]` at the end selects this value.

6. **Initial Call**:
   - The `search` lambda function is initially called with the full range of the array (`left = 0`, `right = len(arr) - 1`), and the result is returned by the `binary_search` function.

7. **Example Usage**:
   - The function can be called with an array and a target value. If the target is found, the function returns its index; otherwise, it returns `-1`.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to recursive stack
- **Style:** Functional, concise lambda expressions
