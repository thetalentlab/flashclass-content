# Recursive Binary Search

## Summary

This recursive binary search variant uses a helper function within the main `binary_search` function. The recursion continues narrowing the search space by adjusting `left` and `right` pointers until the target is found or determined absent, making the function clean and functional.

## Description

This variant implements binary search recursively. The helper function `helper(left, right)` is defined within the main `binary_search` function. The base case for the recursion is when `left` exceeds `right`, indicating that the `target` is not present in the array, in which case the function returns `-1`. If the `target` is found at the middle index, the index is returned. Otherwise, the function recursively calls itself, narrowing down the search space by adjusting the `left` or `right` pointers based on the comparison between `arr[mid]` and `target`.

## Explanation

- **Recursive Function Definition:** The function `binary_search` defines a nested helper function `helper(left, right)` to perform the binary search recursively. This structure allows the main function to remain clean while the recursion logic is encapsulated within the helper function.
- **Base Case:** The base case for the recursion is defined as `if left > right`. This condition checks whether the search space has become invalid (i.e., when the `left` pointer has crossed the `right` pointer). If this condition is met, the function returns `-1`, indicating that the target value is not present in the array.
- **Midpoint Calculation:** The midpoint of the current search space is calculated using the formula `mid = left + (right - left) // 2`. This formula is designed to prevent potential overflow issues that could occur with large indices. The midpoint divides the array into two halves for further searching.
- **Comparison and Recursive Calls:** The function compares the `target` value with the element at the midpoint (`arr[mid]`):
  - If `arr[mid] == target`, the target value has been found, and the function returns the index `mid`.
  - If `arr[mid] < target`, the target is in the right half of the array, so the function recursively calls itself with the new search boundaries `helper(mid + 1, right)`.
  - If `arr[mid] > target`, the target is in the left half of the array, so the function recursively calls itself with the new search boundaries `helper(left, mid - 1)`.
- **Initial Call:** The binary search begins by calling the helper function with the full array as the initial search space: `helper(0, len(arr) - 1)`. This call starts the recursive process that will narrow down the search space until the target is found or determined to be absent.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to recursive stack
- **Style:** Recursive, functional
