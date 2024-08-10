# Binary Search Using the Bisect Module

## Summary

This binary search variant uses Python's `bisect` module to efficiently find the insertion point for the target in a sorted list. It simplifies binary search by returning the index if the target is found, or `-1` otherwise.

## Description

This variant leverages Python's `bisect` module, which is designed for working with sorted lists. The `bisect_left` function finds the insertion point for the `target` in the list to maintain sorted order. If the element at the found index matches the `target`, the index is returned; otherwise, `-1` is returned. This approach abstracts away the binary search logic, making it more concise and Pythonic, while relying on a built-in module.

## Explanation

1. **Importing Bisect**

    The `bisect` module is imported to utilize its binary search functionality.

2. **Finding Insertion Point**

    The `bisect_left` function is used to find the index where the `target` would be inserted to maintain the sorted order of the list. This index is stored in the variable `index`.

3. **Checking Target**

    The code checks whether the `index` is within the bounds of the list and whether the element at that index matches the `target`.

    - If the `target` is found at the computed index, the index is returned.
    - If not, the function returns `-1`, indicating that the `target` is not present in the list.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Utilizes Python's built-in `bisect` module
