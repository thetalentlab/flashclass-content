# Binary Search Using Deque for Stack-Like Behavior

## Summary

This approach demonstrates how Python's `deque` can be used to simulate stack-like behavior in an iterative algorithm, providing flexibility in implementing data structures for algorithmic purposes. The code retains the efficiency of binary search while avoiding recursion by explicitly managing the search intervals with a `deque`.

## Description

This variant of binary search uses a `deque` from the `collections` module to simulate stack behavior. The `deque` is used to store the left and right indices during the search process, mimicking recursion but in an iterative manner. This approach highlights the flexibility of Python's `collections` module in implementing different data structures for algorithmic purposes.

## Explanation

1. **Importing `deque`**:
   - The `deque` class from Python's `collections` module is imported to simulate stack behavior, allowing for efficient additions and removals from both ends.

2. **Deque Initialization**:
   - A `deque` is initialized with a tuple representing the full search interval `(0, len(arr) - 1)`. This tuple contains the `left` and `right` indices, which define the current search boundaries.

3. **Main Search Loop**:
   - The loop continues as long as there are intervals (left, right) to process in the deque. This structure mimics the depth-first nature of recursive calls but avoids the overhead of using the call stack.

4. **Interval Processing**:
   - The `left` and `right` bounds of the current interval are retrieved by popping the last element from the deque, simulating stack behavior.

5. **Midpoint Calculation**:
   - The midpoint is calculated using the formula `mid = left + (right - left) // 2`, a standard binary search operation.

6. **Target Comparison**:
   - If the `target` is found at `arr[mid]`, the function immediately returns `mid`.
   - If `arr[mid]` is less than `target`, the right subarray is pushed onto the deque for further processing.
   - If `arr[mid]` is greater, the left subarray is pushed onto the deque.

7. **Termination**:
   - If the deque becomes empty without finding the target, the function returns `-1`, indicating that the target is not in the array.

8. **Example Usage**:
   - The function can be called with an array and a target value, and it will return the index of the target if found, or `-1` if not.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to the deque
- **Style:** Iterative, stack simulation using deque

