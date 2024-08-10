# Variant 6: Bubble Sort Using Recursion

This variant of bubble sort is implemented recursively. Instead of iterating over the array using loops, the function calls itself with a reduced size of the unsorted portion of the array. The recursion continues until the entire array is sorted. This approach offers a different perspective on the bubble sort algorithm but is less efficient in terms of space due to the recursion stack.

### Characteristics:
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(n) due to recursion stack
- **Style:** Recursive, alternative to iterative approach
