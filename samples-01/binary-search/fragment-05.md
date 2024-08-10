# Variant 5: Binary Search Using the Bisect Module

This variant leverages Python's `bisect` module, which is designed for working with sorted lists. The `bisect_left` function finds the insertion point for the `target` in the list to maintain sorted order. If the element at the found index matches the `target`, the index is returned; otherwise, `-1` is returned. This approach abstracts away the binary search logic, making it more concise and Pythonic, while relying on a built-in module.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Utilizes Python's built-in `bisect` module
