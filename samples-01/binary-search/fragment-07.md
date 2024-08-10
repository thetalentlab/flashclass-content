# Variant 7: Iterative Binary Search with Manual Stack

In this variant, binary search is performed iteratively but uses a manual stack to track the search intervals, mimicking the behavior of recursion. Instead of relying on the call stack, a custom stack (a list) is used to store tuples representing the left and right bounds of the search space. The stack-based approach can be particularly useful when you want to avoid the overhead of recursion while retaining some of its conceptual clarity.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to the manual stack
- **Style:** Iterative, mimics recursion with a manual stack
