# Binary Search Using Recursion with Reversed Boundaries

## Summary

This variant of binary search is unconventional, as it reverses the traditional roles of the `left` and `right` pointers, demonstrating the flexibility of recursion. The logic remains similar to standard binary search but is mirrored, making it an interesting and educational example of how recursive algorithms can be adapted in creative ways.

## Description

This variant implements binary search with reversed boundaries, where the `left` and `right` indices start from the end and beginning of the array, respectively. The calculation of the middle index is also adjusted to reflect this reversal. The recursive logic remains similar to traditional binary search but is mirrored, making it an interesting variation that demonstrates the flexibility of recursion.

## Explanation

1. **Helper Function**:
   - A nested `helper` function is defined within `binary_search` to handle the recursive search process. It takes `right` and `left` as arguments, with their roles reversed from traditional binary search.

2. **Base Case**:
   - The base case checks if the search space is invalid by comparing if `right < left`. If true, the function returns `-1`, indicating the target is not found.

3. **Reversed Midpoint Calculation**:
   - The midpoint is calculated using `mid = right - (right - left) // 2`. This calculation is adjusted to reflect the reversed roles of `right` and `left`.

4. **Target Comparison**:
   - If the target is found at `arr[mid]`, the function returns `mid`.
   - If `arr[mid]` is less than `target`, the function recursively searches the right half using the reversed logic (`right, mid + 1`).
   - If `arr[mid]` is greater, the function recursively searches the left half using the reversed logic (`mid - 1, left`).

5. **Initial Call**:
   - The binary search begins by calling `helper` with `right` initialized to the last index of the array (`len(arr) - 1`) and `left` initialized to the first index (`0`), reflecting the reversed boundaries.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to recursive stack
- **Style:** Recursive, unconventional reversed boundaries

