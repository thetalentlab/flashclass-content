# Binary Search with a While-Else Loop

## Summary

This binary search variant uses a `while-else` loop, where the `else` block executes if the search loop completes without finding the target. It highlights Python's unique `while-else` construct, returning `-1` when the target isn't found.

## Description

This variant introduces a slight modification to the iterative binary search by utilizing a `while-else` loop. The `else` block executes if the `while` loop completes without encountering a `break` statement. This is particularly useful here to return `-1` when the search completes without finding the target. The core logic remains the same, but this approach emphasizes the use of Python's unique `while-else` construct, which is less commonly used in basic binary search implementations.

## Explanation

- **Initialization:** The `left` and `right` pointers are initialized to the bounds of the array (`0` and `len(arr) - 1`).
- **While Loop:** The loop continues as long as `left` is less than or equal to `right`, meaning there is still a valid range to search within.
- **Mid Calculation:** The midpoint is calculated using `mid = left + (right - left) // 2`.
- **Condition Checks:**
  - If `arr[mid] == target`, the function returns `mid`, indicating the target has been found.
  - If `arr[mid] < target`, the search continues in the right half by updating `left`.
  - If `arr[mid] > target`, the search continues in the left half by updating `right`.
- **Else Block:** If the loop completes without finding the target (i.e., the loop condition fails), the `else` block is executed, returning `-1` to indicate that the target is not present in the array.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, procedural with a Pythonic twist
