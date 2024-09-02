# Iterative Binary Search with Manual Stack

## Summary

This approach provides a clear iterative alternative to recursion, retaining the conceptual simplicity of recursive binary search while being explicit about the search intervals using a manual stack.

## Description

In this variant, binary search is performed iteratively but uses a manual stack to track the search intervals, mimicking the behavior of recursion. Instead of relying on the call stack, a custom stack (a list) is used to store tuples representing the left and right bounds of the search space. The stack-based approach can be particularly useful when you want to avoid the overhead of recursion while retaining some of its conceptual clarity.

## Explanation

1. **Stack Initialization**

    The stack is initialized with a tuple representing the full search interval `(0, len(arr) - 1)`. This tuple contains the `left` and `right` indices, which define the current search boundaries.

2. **Main Search Loop**

    The loop continues as long as there are intervals to process in the stack. This mimics the depth-first nature of recursive calls but avoids the overhead of using the call stack.

3. **Interval Processing**

    The `left` and `right` bounds of the current interval are retrieved by popping the last element from the stack. This ensures that the most recently added interval is processed first (LIFO behavior).

4. **Midpoint Calculation**

    The midpoint is calculated using the formula `mid = left + (right - left) // 2` to avoid potential overflow issues. This index is the point where the search divides the array.

5. **Target Comparison**

    - If the target is found at `arr[mid]`, the function immediately returns `mid`.
    - If the target is greater than `arr[mid]`, the search continues in the right subarray, which is added to the stack.
    - If the target is smaller, the search continues in the left subarray, which is similarly added to the stack.

6. **Termination**

    If the stack becomes empty without finding the target, the function returns `-1`, indicating that the target is not in the array.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to the manual stack
- **Style:** Iterative, mimics recursion with a manual stack

