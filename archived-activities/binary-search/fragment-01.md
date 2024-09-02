# Basic Iterative Binary Search

## Summary

This basic iterative binary search uses two pointers to track the search boundaries in a sorted array. It repeatedly recalculates the midpoint and adjusts the search range until the target is found or the search space is exhausted, providing an efficient and straightforward approach.

## Description

This implementation of binary search is a straightforward iterative approach. The function takes a sorted array `haystack` and a `needle` value. It uses two pointers, `left` and `right`, to track the search boundaries. The mid-point is recalculated on each iteration as `mid = left + (right - left) // 2`. Depending on whether the `needle` is less than, greater than, or equal to the middle element, the function adjusts the search range by updating either the `left` or `right` pointer. This process continues until the target is found or the search space is exhausted.

## Explanation

- **Initialization:** The left pointer is set to the start of the array (0), and the right pointer is set to the end (`len(haystack) - 1`).
- **Loop Condition:** The loop continues as long as `left` is less than or equal to `right`, meaning there's still a valid range to search.
- **Mid Calculation:** The midpoint is recalculated each iteration as `mid = left + (right - left) // 2` to avoid potential overflow issues.
- **Comparison:** If the target is found at `mid`, the function returns the index `mid`. If the target is less than `arr[mid]`, the search range is updated to the left half by setting `right = mid - 1`. Otherwise, it’s updated to the right half by setting `left = mid + 1`.
- **Termination:** If the loop exits without finding the target, the function returns `-1`, indicating that the target is not in the array.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, procedural
