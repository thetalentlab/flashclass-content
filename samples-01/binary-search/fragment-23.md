# Binary Search with a Custom Comparator

## Summary

This variant of binary search is highly flexible, allowing the user to define custom comparison logic via the `comparator` function. By default, it behaves like a standard numeric binary search, but the ability to pass in different comparator functions makes it adaptable for a wide range of data types and search criteria. The detailed comments help clarify how the comparator is integrated into the binary search process.

## Description

This variant allows for a custom comparator function to be passed in, which determines how the elements should be compared. By default, it uses a lambda function that simply subtracts the target from the current array element. This approach makes the binary search more flexible, allowing it to be used with different types of data and comparison logic.

## Explanation

1. **Function Definition**:
   - The `binary_search` function is defined to take three arguments: `arr` (the array to search), `target` (the value to find), and an optional `comparator` function.
   - The `comparator` function defaults to `lambda x, y: x - y`, which performs a simple subtraction, suitable for numeric comparisons.

2. **Initialization**:
   - The `left` pointer is initialized to the start of the array (`0`), and the `right` pointer is initialized to the end of the array (`len(arr) - 1`).

3. **Binary Search Loop**:
   - The loop continues as long as the `left` pointer is less than or equal to the `right` pointer, ensuring there is still a valid range to search within.

4. **Midpoint Calculation**:
   - The midpoint `mid` is calculated using the formula `mid = left + (right - left) // 2`, which is a standard approach in binary search.

5. **Comparison Using Custom Comparator**:
   - The `comparator` function is used to compare the midpoint element (`arr[mid]`) with the `target`.
   - The result of the `comparator` is stored in the `comparison` variable:
     - If `comparison == 0`, it means `arr[mid]` equals `target`, so the function returns `mid`.
     - If `comparison < 0`, it means `arr[mid]` is less than `target`, so the search continues in the right half by adjusting the `left` pointer.
     - If `comparison > 0`, it means `arr[mid]` is greater than `target`, so the search continues in the left half by adjusting the `right` pointer.

6. **Termination**:
   - If the loop exits without finding the target, the function returns `-1`, indicating that the target is not present in the array.

7. **Example Usage**:
   - **Default Comparator**: The function can be used with the default comparator for numeric comparisons, returning the index of the target if found, or `-1` if not.
   - **Custom Comparator**: The function can also be used with a custom comparator, such as comparing string lengths or other custom comparison logic, making it versatile for different data types and comparison rules.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, flexible with custom comparator
