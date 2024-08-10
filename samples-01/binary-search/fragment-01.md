# Basic Iterative Binary Search

This implementation of binary search is a straightforward iterative approach. The function takes a sorted array `arr` and a `target` value. It uses two pointers, `left` and `right`, to track the search boundaries. The mid-point is recalculated on each iteration as `mid = left + (right - left) // 2`. Depending on whether the `target` is less than, greater than, or equal to the middle element, the function adjusts the search range by updating either the `left` or `right` pointer. This process continues until the target is found or the search space is exhausted.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, procedural