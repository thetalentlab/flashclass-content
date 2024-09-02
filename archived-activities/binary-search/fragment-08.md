# Binary Search Using a For Loop

## Summary

This variant of binary search demonstrates an unconventional use of a `for` loop to perform the iterative search, which is different from the typical `while` loop approach. The `for` loop structure allows for a fixed number of iterations but includes a mechanism to exit early if the search space is no longer valid.

## Description

This variant utilizes a `for` loop instead of the more common `while` loop. The `for` loop iterates a fixed number of times (equal to the length of the array), which is somewhat unconventional for binary search. The loop breaks early if the search space is exhausted (`left > right`). This variant highlights an alternative way to structure the iteration process.

## Explanation

1. **Initialization**:
   - The `left` pointer is set to the start of the array (`0`), and the `right` pointer is set to the end of the array (`len(arr) - 1`).

2. **For Loop**:
   - A `for` loop iterates a fixed number of times, equal to the length of the array (`len(arr)`). This is unconventional for binary search, which typically uses a `while` loop.
   - The loop is structured so that it can exit early if the search space is exhausted (`left > right`).

3. **Midpoint Calculation**:
   - The midpoint is calculated in each iteration using the formula `mid = left + (right - left) // 2`.

4. **Target Comparison**:
   - If `arr[mid] == target`, the function returns the index `mid`.
   - If `arr[mid] < target`, the search continues in the right half by adjusting the `left` pointer.
   - If `arr[mid] > target`, the search continues in the left half by adjusting the `right` pointer.

5. **Termination**:
   - If the loop completes without finding the target, the function returns `-1`, indicating that the target is not in the array.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, unconventional use of `for` loop
