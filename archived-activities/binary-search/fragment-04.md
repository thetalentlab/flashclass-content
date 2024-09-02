# Binary Search Using Slicing in Recursion

## Summary

This recursive binary search variant uses Python's slicing to search the left or right half of the array after calculating the midpoint. While it simplifies recursion, slicing can increase space complexity by creating new sublists, potentially impacting efficiency for large arrays.

## Description

This variant uses Python's slicing capabilities to implement binary search recursively. After calculating the middle index, the array is sliced either from the start to the middle (for searching the left half) or from the middle to the end (for searching the right half). This approach simplifies the recursion but may increase the space complexity since slicing creates new lists, which can be inefficient for large arrays.

## Explanation

1. **Base Case**

    If the input array is empty (`not arr`), the function returns `-1` to indicate that the target is not found.

2. **Mid Calculation**

    The midpoint of the array is calculated using `mid = len(arr) // 2`.

3. **Target Check**

    If the target is found at `arr[mid]`, the function returns `mid`.

4. **Left Half Search**

    - If the target is smaller than `arr[mid]`, the function recursively searches the left half by slicing the array with `arr[:mid]`.
    - The function returns the result of this recursive call.

5. **Right Half Search**

    - If the target is larger than `arr[mid]`, the function recursively searches the right half by slicing the array with `arr[mid+1:]`.
    - The function adjusts the result index by adding `mid + 1` to account for the sliced portion of the array.
    - If the target is found, it returns the adjusted index; otherwise, it returns `-1`.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to slicing and recursive stack
- **Style:** Recursive, Pythonic, uses slicing
