# Binary Search Using a Dictionary to Store Search History

## Summary

This variant of binary search emphasizes tracking the search process by storing the history of examined indices and their values in a dictionary. While this approach doesn't enhance performance, it provides a clear way to understand and debug the binary search algorithm by capturing the intermediate states. The detailed comments and debugging output help illustrate how the search progresses, making it a valuable tool for learning and analysis.

## Description

In this variant, a dictionary is used to store the indices and their corresponding values during the search. This is more of a pedagogical approach to show how one could track the search history. It doesn't offer performance benefits but demonstrates how you can capture intermediate states in an algorithm, which can be useful for debugging or analysis.

## Explanation

1. **Search History Dictionary**:
   - A dictionary `search_history` is initialized to store the indices (`mid`) and their corresponding values (`arr[mid]`) during the search process.
   - This dictionary captures the intermediate states of the search, which can be useful for debugging or analyzing how the algorithm navigates through the array.

2. **Initialization**:
   - **Left Pointer**: Set to `0`, representing the start of the array.
   - **Right Pointer**: Set to `len(arr) - 1`, representing the end of the array.

3. **Iterative Search Process**:
   - The loop continues as long as `left <= right`, meaning there is still a valid range to search.

4. **Midpoint Calculation**:
   - The midpoint `mid` is calculated as `left + (right - left) // 2`, which is the standard approach in binary search.

5. **Storing Search History**:
   - The current midpoint index and its value are stored in the `search_history` dictionary using `search_history[mid] = arr[mid]`.
   - This allows you to track which parts of the array have been examined during the search.

6. **Debugging Output**:
   - A `print` statement is included to display the current state of `search_history` after each iteration, providing insights into the search process.

7. **Target Comparison**:
   - **Target Found**: If `arr[mid]` equals the `target`, the function returns `mid`, the index where the target is found.
   - **Target Greater**: If `arr[mid]` is less than `target`, the search space is reduced to the right half by moving the `left` pointer to `mid + 1`.
   - **Target Smaller**: If `arr[mid]` is greater than `target`, the search space is reduced to the left half by moving the `right` pointer to `mid - 1`.

8. **Termination**:
   - The loop exits when `left` exceeds `right`, meaning the search space is exhausted. If this happens without finding the target, return `-1` to indicate that the target is not in the array.

9. **Example Usage**:
   - The function can be used by passing a sorted array and a target value. If the target is found, the function returns its index; otherwise, it returns `-1`.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to the dictionary
- **Style:** Iterative, tracks search history in a dictionary
