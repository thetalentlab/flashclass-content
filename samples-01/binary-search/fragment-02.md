# Recursive Binary Search

This variant implements binary search recursively. The helper function `helper(left, right)` is defined within the main `binary_search` function. The base case for the recursion is when `left` exceeds `right`, indicating that the `target` is not present in the array, in which case the function returns `-1`. If the `target` is found at the middle index, the index is returned. Otherwise, the function recursively calls itself, narrowing down the search space by adjusting the `left` or `right` pointers based on the comparison between `arr[mid]` and `target`.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to recursive stack
- **Style:** Recursive, functional
